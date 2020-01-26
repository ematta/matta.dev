<template>
  <div>
    <p>Hey {{ user.name }}</p>
  </div>
</template>

<script>
import { mapState } from 'vuex';

export default {
  name: 'Profile',
  computed: mapState(['user']),
  beforeCreate() {
    this.$store.dispatch('checkIfLoggedInAlready');
  },
};
</script>
