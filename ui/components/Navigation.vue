<template>
  <div class="hero hero-body is-primary" id="app">
    <section >
      {{ $log(`Auth Checl ${authCheck()}`) }}
      <div v-if="authCheck()  ">
        <router-link class="nav-item nav-word" :to="{ name: 'Profile' }">Profile</router-link>
        <router-link class="nav-item nav-word" :to="{ name: 'Logout' }">Logout</router-link>
      </div>
      <div v-else>
        <router-link class="nav-item nav-word" :to="{ name: 'Login' }">Login</router-link>
        <router-link class="nav-item nav-word" :to="{ name: 'Register' }">Register</router-link>
      </div>
    </section>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Navigation',
  computed: mapState(['isAuthenticated', 'user']),
  methods: {
    authCheck() {
      return this.isAuthenticated && this.user;
    },
  },
};
</script>
