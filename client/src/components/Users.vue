<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-sm-10">
        <div v-if="loggedIn">
          <h3>Welcome back {{ user['username'] }}</h3>
          <h5>Wanna logout?</h5>
          <button type="button"
                  class="btn btn-primary"
                  v-on:click="initForm">
            Logout
          </button>
        </div>
        <div v-else>
          <h1>Log In</h1>
          <hr>
          <br><br>
          <h3>Welcome back!</h3>
          <button type="button"
                  class="btn btn-primary"
                  v-b-modal.login-modal>
            Log In
          </button>
          <alert :message="message" v-if="showMessage"></alert>
          <hr>
          <br><br>
          <h3>New here?</h3>
          <button type="button"
                  class="btn btn-primary">
            Sign Up
          </button>
        </div>
      </div>
    </div>
    <b-modal ref="loginModal"
             id="login-modal"
             title="Login"
             hide-footer>
      <b-form @submit="onLogin" @reset="onReset" class="w-100">
        <b-form-group id="form-username-group"
                      label="Username:"
                      label-for="form-username-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="loginForm.username"
                        required
                        placeholder="Enter your username here">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="Password:"
                      label-for="form-password-input">
          <b-form-input id="form-password-input"
                        type="password"
                        v-model="loginForm.password"
                        required
                        placeholder="Enter your password here">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';
import Navbar from './Navbar.vue';

export default {
  data() {
    return {
      user: [],
      loggedIn: false,
      loginForm: {
        username: '',
        password: '',
      },
      message: '',
      showMessage: false,
      path: 'http://localhost:5000/login',
    };
  },

  components: {
    Alert,
    Navbar,
  },

  methods: {
    onLogin(evt) {
      evt.preventDefault();
      this.$refs.loginModal.hide();

      const payload = {
        username: this.loginForm.username,
        password: this.loginForm.password,
      };

      this.login(payload);
    },

    login(payload) {
      axios.put(this.path, payload)
        .then((res) => {
          this.user = res.data.user;
          this.message = res.data.message;
          this.showMessage = true;

          if (this.user !== undefined) {
            this.loggedIn = true;
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },

    onReset(evt) {
      evt.preventDefault();
      this.$refs.loginModal.hide();
      this.initForm();
    },

    initForm() {
      this.loginForm.username = '';
      this.loginForm.password = '';
      this.user = [];
      this.message = '';
      this.showMessage = false;
      this.loggedIn = false;
    },
  },
};
</script>

<style scoped>

</style>
