import Vue from 'vue';
import Vuex from 'vuex';
import router from '@/router';
import {
  checkIfLoggedInAlreadyApi,
  loginUserApi,
  registerUserApi,
} from '@/api';
import { isValidToken, tokenGetExpireTime } from '@/utility';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    token: '',
    user: {},
    errorMessage: '',
    isAuthenticated: false,
  },
  actions: {
    login(context, payload) {
      return loginUserApi(payload)
        .then((response) => {
          context.commit('setToken', response.data.token);
          context.commit('setUser', response.data.user);
          context.commit('setIsAuthenticated', isValidToken(response.data.token));
          Vue.$cookies.set('token', response.data.token, tokenGetExpireTime(response.data.token));
        })
        .catch((error) => {
          context.commit('setErrorMessage', error);
        });
    },
    logout(context) {
      return new Promise((resolve) => {
        Vue.$cookies.remove('token');
        context.commit('setToken', '');
        context.commit('setUser', {});
        context.commit('setIsAuthenticated', false);
        resolve();
      });
    },
    checkIfLoggedInAlready(context) {
      const token = Vue.$cookies.get('token');
      let check = null;
      if (token && isValidToken(token)) {
        check = checkIfLoggedInAlreadyApi(token)
          .then((response) => {
            context.commit('setUser', response.data.user);
            context.commit('setToken', token);
            context.commit('setIsAuthenticated', isValidToken(response.data.token));
          })
          .catch((error) => {
            context.commit('setUser', {});
            context.commit('setToken', '');
            context.commit('setIsAuthenticated', false);
            context.commit('setErrorMessage', error);
          });
      } else {
        context.commit('setUser', {});
        context.commit('setToken', '');
        context.commit('setIsAuthenticated', false);
        router.push({ name: 'Login' });
      }
      return check;
    },
    registerUser(context, user) {
      return registerUserApi(user)
        .then(() => {
          router.push({ name: 'Login' });
        })
        .catch((error) => {
          context.commit('setErrorMessage', error);
        });
    },
  },
  mutations: {
    setErrorMessage(state, errorMessage) {
      state.errorMessage = errorMessage;
    },
    setToken(state, token) {
      state.token = token;
    },
    setUser(state, user) {
      state.user = user;
    },
    setIsAuthenticated(state, status) {
      state.isAuthenticated = status;
    },
  },
  getters: {
    token: state => state.token,
    user: state => state.user,
    isAuthenticated: state => state.isAuthenticated,
  },
});

export default store;
