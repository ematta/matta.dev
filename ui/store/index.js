import Vue from 'vue';
import Vuex from 'vuex';
import router from '@/router';
import {
  getUserInfoApi,
  loginUserApi,
  registerUserApi,
} from '@/api';
import { isValidJwt, jwtGetExpireTime } from '@/utility';

Vue.use(Vuex);

const store = new Vuex.Store({
  state: {
    jwt: '',
    user: {},
    errorMessage: '',
    isAuthenticated: false,
  },
  actions: {
    login(context, user) {
      return loginUserApi(user)
        .then((response) => {
          context.commit('setJwt', response.data);
        })
        .catch((error) => {
          context.commit('setErrorMessage', error);
        });
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
    getUserInfo(context) {
      return getUserInfoApi(context.state.jwt)
        .then((response) => {
          context.commit('setUser', response);
        })
        .catch((error) => {
          context.commit('setErrorMessage', error);
        });
    },
    checkIfLoggedInAlready(context) {
      return new Promise((resolve) => {
        const token = Vue.$cookies.get('token');
        if (token && isValidJwt(token)) {
          context.commit('setJwtSansCookie', token);
          resolve();
        }
      })
        .then(() => {
          context.dispatch('getUserInfo');
        });
    },
  },
  mutations: {
    setErrorMessage(state, errorMessage) {
      state.errorMessage = errorMessage;
    },
    setJwt(state, payload) {
      state.jwt = payload.token;
      state.user = payload.user;
      state.isAuthenticated = isValidJwt(payload.token);
      Vue.$cookies.set('token', payload.token, jwtGetExpireTime(payload.token));
    },
    setJwtSansCookie(state, token) {
      state.jwt = token;
      state.isAuthenticated = isValidJwt(token);
    },
    setUser(state, user) {
      state.user.name = user.data.user.name;
      state.user.email = user.data.user.email;
      state.user.id = user.data.user.id;
    },
    logout(state) {
      state.jwt = '';
      state.user = {};
      state.isAuthenticated = false;
      Vue.$cookies.remove('token');
    },
  },
  getters: {
    jwt: state => state.jwt,
    user: state => state.user,
    isAuthenticated: state => state.isAuthenticated,
  },
});

export default store;
