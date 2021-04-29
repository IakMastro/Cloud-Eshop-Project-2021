<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-sm-20">
        <h2>LIBRARY</h2>
        <hr>
        <br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">OWNED GAMES</th>
            <th scope="col">FAVOURITE</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr>
          <tr v-for="(game, index) in games" :key="index">
            <td>{{ game.title }}</td>
           <td>
           <label
                class="favorite__heart"
                v-bind:class="{'favorite__heart__selected': value, 'is-disabled': disabled}"
                v-on:click="favorite">
            <input
                    class="favorite__checkbox"
                    type="checkbox"
                    v-bind:name="name"
                    v-bind:value="value"
                    v-bind:required="required"
                    v-bind:disabled="disabled"
                    v-model="value">
            &#10084;&#65039;
        </label>
              </td>
            <td>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>
<script>

import axios from 'axios';
import Navbar from './Navbar.vue';

export default {
  // Data used on this page
  data() {
    return {
      games: [],
      gameForm: {
        id: '',
        title: '',
        developer: '',
        favourite: [],
        edit: [],
      },
      message: '',
      showMessage: false,
      path: 'http://localhost:5000/admin',
    };
  },

  // Templates that exist on other file
  components: {
    navbar: Navbar,
  },
  props: ['is_fav'],
  // Methods used on this page
  methods: {
    togglefav() {
      this.$emit('togglefav', !this.is_fav);
    },
    // Get: gets all the games
    getGames() {
      axios.get(this.path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((error) => {
          console.error(error);
        });
    },
  },

  // It is used when the page is loaded for the first time.
  created() {
    this.getGames();
  },
};
</script>
