<template>
  <div class="container-fluid">
    <navbar></navbar>
    <div v-if="loggedIn">
      <div class="col-sm-8">
        <h3>Welcome back {{ user['username'] }}</h3>
        <h5>Wanna logout?</h5>
        <button type="button"
                class="btn btn-primary"
                v-on:click="initForm">
          Logout
        </button>
      </div>
    </div>
    <div v-else>
      <alert :message="message" v-if="showMessage"></alert>
      <div class="row no-gutters">
        <div class="d-none d-md-flex col-md-4 col-lg-6 bg-image">
        </div>
        <div class="col-md-8 col-lg-6">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-md-9 col-lg-8 mx-auto">
                  <h3 class="login-heading mb-4">Welcome Back!</h3>
                  <form>
                    <div class="form-label-group">
                      <input type="text" id="inputUsername" class="form-control"
                             placeholder="Username" required autofocus>
                      <label for="inputUsername">Username</label>
                    </div>

                    <div class="form-label-group">
                      <input type="password" id="inputPassword" class="form-control"
                             placeholder="Password" required>
                      <label for="inputPassword">Password</label>
                    </div>

                    <div class="custom-control custom-checkbox mb-3">
                      <input type="checkbox" class="custom-control-input" id="rememberMe">
                      <label class="custom-control-label" for="rememberMe">Remember password</label>
                    </div>

                    <button type="button"
                            class="btn btn-lg btn-primary btn-block btn-login
                      text-uppercase font-weight-bold mb-2" v-on:click="onLogin">
                      Log In
                    </button>
                    <div class="text-center">
                      <a class="small" href="#">Forgot Password?</a>
                    </div>
                  </form>
                  <hr>
                  <h3 class="login-heading mb-4">New here?</h3>
                  <button class="btn btn-lg btn-primary btn-block btn-login text-uppercase
                  font-weight-bold mb-2">
                    Sign up
                  </button>
                </div>
              </div>
            </div>
          </div>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import $ from 'jquery';
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
      path: 'http://localhost:5001/login',
    };
  },

  components: {
    Alert,
    Navbar,
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
:root {
  --input-padding-x: 1.5rem;
  --input-padding-y: 0.75rem;
}

.login,
.image {
  min-height: 100vh;
}

.bg-image {
  background-image: url('https://source.unsplash.com/WEQbe2jBg40/600x1200');
  background-size: cover;
  background-position: center;
}

.login-heading {
  font-weight: 300;
}

.btn-login {
  font-size: 0.9rem;
  letter-spacing: 0.05rem;
  padding: 0.75rem 1rem;
  border-radius: 2rem;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group > input,
.form-label-group > label {
  padding: var(--input-padding-y) var(--input-padding-x);
  height: auto;
  border-radius: 2rem;
}

.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0;
  /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  cursor: text;
  /* Match the input under the label */
  border: 1px solid transparent;
  border-radius: .25rem;
  transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: calc(var(--input-padding-y) + var(--input-padding-y) * (2 / 3));
  padding-bottom: calc(var(--input-padding-y) / 3);
}

.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: calc(var(--input-padding-y) / 3);
  padding-bottom: calc(var(--input-padding-y) / 3);
  font-size: 12px;
  color: #777;
}

/* Fallback for Edge
-------------------------------------------------- */

@supports (-ms-ime-align: auto) {
  .form-label-group > label {
    display: none;
  }

  .form-label-group input::-ms-input-placeholder {
    color: #777;
  }
}

/* Fallback for IE
-------------------------------------------------- */

@media all and (-ms-high-contrast: none),
(-ms-high-contrast: active) {
  .form-label-group > label {
    display: none;
  }

  .form-label-group input:-ms-input-placeholder {
    color: #777;
  }
}
</style>
