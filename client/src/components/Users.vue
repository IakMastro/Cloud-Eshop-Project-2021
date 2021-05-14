<template>
  <div class="container-fluid">
    <navbar></navbar>
    <login></login>
  </div>
</template>

<script>
/* eslint-disable*/
import Alert from './Alert.vue';
import Navbar from './Navbar.vue';
import Login from './Login.vue';

export default {
  data() {
    return {};
  },

  components: {
    Alert,
    Navbar,
    Login
  }
}
</script>

<style scoped>

</style>
