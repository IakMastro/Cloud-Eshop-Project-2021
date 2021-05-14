<template>
  <div class="container">
    <alert :message="message" v-if="showMessage"></alert>
    <h5>Welcome back!</h5>

    <div class="form-group">
      <label for="email">Username:</label>
      <input type="email" class="form-control" id="email" placeholder="Enter email" name="email">
    </div>

    <div class="form-group">
      <label for="pwd">Password:</label>
      <input type="password" class="form-control" id="pwd" placeholder="Enter password" name="pwd">
    </div>

    <button type="submit"
            class="btn btn-primary"
            @click="onLogin">
      Log In
    </button>

    <hr>
    <h5>New here?</h5>
    <button type="button"
            class="btn btn-primary"
            v-b-modal.signup-modal>
      Sign Up
    </button>

    <b-modal ref="singUpModal"
             id="signup-modal"
             title="Enter your credentials"
             hide-footer>
      <b-form @submit="onSignUp" @reset="resetRegisterForm" class="w-100">
        <b-form-group id="form-username-group"
                      label="Username:"
                      label-for="form-username-input">
          <b-form-input id="form-username-input"
                        type="text"
                        v-model="registerForm.username"
                        required
                        placeholder="Enter username">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-password-group"
                      label="Password:"
                      label-for="form-password-input">
          <b-form-input id="form-password-input"
                        type="password"
                        v-model="registerForm.password"
                        required
                        placeholder="Enter password">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-repeatPwd-group"
                      label="Repeat password:"
                      label-for="form-repeatPwd-input">
          <b-form-input id="form-repeatPwd-input"
                        type="password"
                        v-model="registerForm.repeatPwd"
                        required
                        placeholder="Enter password again">
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
/* eslint-disable*/
import axios from 'axios';
import Alert from './Alert.vue';
import $ from 'jquery';

export default {
  name: 'Login',
  data() {
    return {
      user: [],
      loginForm: {
        username: '',
        password: '',
      },
      registerForm: {
        username: '',
        password: '',
        repeatPwd: '',
      },
      message: '',
      showMessage: false,
      path: 'http://localhost:5001',
    };
  },

  components: {
    Alert,
  },

  methods: {
    onLogin() {
      const payload = {
        username: $('#inputUsername').val(),
        password: $('#inputPassword').val(),
      };

      this.login(payload);
    },

    login(payload) {
      axios.put('http://localhost:5001/login', payload)
        .then((res) => {
          this.user = res.data.user;
          this.message = res.data.message;
          this.showMessage = true;

          if (this.user !== undefined) {
            console.log("Logged in!")
          }
        })
        .catch((error) => {
          console.error(error);
        });
    },

    initForm() {
      this.loginForm.username = '';
      this.loginForm.password = '';
      this.registerForm.username = '';
      this.registerForm.password = '';
      this.registerForm.repeatPwd = '';
      this.user = [];
      this.message = '';
      this.showMessage = false;
    },

    resetRegisterForm() {
      this.registerForm.username = '';
      this.registerForm.password = '';
      this.registerForm.repeatPwd = '';
    },

    onSignUp(evt) {
      evt.preventDefault();
      this.$refs.signUpModal.hide();

      if (this.registerForm.password === this.registerForm.repeatPwd) {
        const payload = {
          username: this.registerForm.username,
          password: this.registerForm.password,
        };

        this.signup(payload);
      } else {
        this.message = 'Passwords must match';
      }
    },

    signup(payload) {
      axios.post(this.path + '/signup', payload)
        .then((res) => {
          this.message = res.data.message;
          this.resetRegisterForm();
          this.showMessage = true;
        });
    },
  },
};
</script>

<style scoped>

</style>
