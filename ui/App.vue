<template>
  <div id="app">
    {{ $log(`Error Message: ${errorMessage}`) }}
    <Navigation />
    <router-view />
  </div>
</template>

<script>
import { mapState } from 'vuex';
import Navigation from '@/components/Navigation.vue';

export default {
  name: 'App',
  computed: mapState(['errorMessage']),
  components: {
    Navigation,
  },
  beforeCreate() {
    this.$store.dispatch('checkIfLoggedInAlready');
  },
  methods: {
    clearMessage() {
      this.$store.commit('setErrorMessage', '');
    },
  },
};
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 30px;
}
</style>
