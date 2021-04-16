<template>
  <div class="container">
    <navbar></navbar>
    <div class="row">
      <div class="col-sm-20">
        <h1>Games</h1>
        <hr>
        <br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button"
                class="btn btn-danger btn-md"
                v-b-modal.game-modal>
          Add Game
        </button>
        <br><br>
        <table class="table table-hover">
          <thead>
          <tr>
            <th scope="col">Title</th>
            <th scope="col">Developer</th>
            <th scope="col">Favoured?</th>
            <th></th>
          </tr>
          </thead>
          <tbody>
          <tr>
          <tr v-for="(game, index) in games" :key="index">
            <td>{{ game.title }}</td>
            <td>{{ game.developer }}</td>
            <td>
              <span v-if="game.favoured">Yes</span>
              <span v-else>No</span>
            </td>
            <td>
              <div class="btn-group" role="group">
                <button type="button"
                        class="btn btn-info btn-sm"
                        v-b-modal.game-modal
                        @click="editGame(game)">
                  Update
                </button>
                <button type="button"
                        class="btn btn-danger btn-sm"
                        @click="onDeleteGame(game.id)">
                  Delete
                </button>
              </div>
            </td>
          </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addGameModal"
             id="game-modal"
             title="Add a new game"
             hide-footer>
      <b-form @submit="onsubmit" @reset="onreset" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="gameForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-developer-group"
                      label="Developer:"
                      label-for="form-developer-input">
          <b-form-input id="form-developer-input"
                        type="text"
                        v-model="gameForm.developer"
                        required
                        placeholder="Enter developer">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="gameForm.favoured" id="form-checks">
            <b-form-checkbox value="true">Favoured?</b-form-checkbox>
          </b-form-checkbox-group>
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
  // Data used on this page
  data() {
    return {
      games: [],
      gameForm: {
        id: '',
        title: '',
        developer: '',
        favoured: [],
        edit: [],
      },
      message: '',
      showMessage: false,
      path: 'http://localhost:5000/admin',
    };
  },

  // Templates that exist on other file
  components: {
    alert: Alert,
    navbar: Navbar,
  },

  // Methods used on this page
  methods: {
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

    // Post: adds a new game on the database
    addGame(payload) {
      axios.post(this.path, payload)
        .then(() => {
          this.getGames();
          this.message = 'Game added!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.message = 'No connection to server';
          this.showMessage = true;
          this.getGames();
        });
    },

    // Initialize the form
    initForm() {
      this.gameForm.id = '';
      this.gameForm.title = '';
      this.gameForm.developer = '';
      this.gameForm.favoured = [];
      this.gameForm.edit = false;

      this.getGames();
    },

    // Submitting the form
    onsubmit(evt) {
      evt.preventDefault();
      this.$refs.addGameModal.hide();

      let favoured = false;

      if (this.gameForm.favoured[0]) favoured = true;

      const payload = {
        id: this.gameForm.id,
        title: this.gameForm.title,
        developer: this.gameForm.developer,
        favoured,
      };

      // If the form we completed is for editing, then updateGame works.
      // Otherwise, it adds the game.
      if (this.gameForm.edit) {
        this.updateGame(payload, payload.id);
      } else {
        this.addGame(payload);
      }

      this.initForm();
    },

    // Resets the form, in case of a mistake
    onreset(evt) {
      evt.preventDefault();
      this.initForm();
    },

    // Put: updates the info for the selected game.
    updateGame(payload, gameId) {
      const path = this.path.concat(`/${gameId}`);
      axios.put(path, payload)
        .then(() => {
          this.getGames();
          this.message = 'Game updated!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getGames();
        });
    },

    // Delete: deletes the game from the database
    removeGame(gameID) {
      const path = this.path.concat(`/${gameID}`);

      axios.delete(path)
        .then(() => {
          this.getGames();
          this.message = 'Game removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.error(error);
          this.getGames();
        });
    },

    // Removes the game from the array locally.
    onDeleteGame(game) {
      this.removeGame(game);
    },

    // It's called to get the info for the game to be edited.
    editGame(game) {
      this.gameForm = game;
      this.gameForm.edit = true;
    },
  },

  // It is used when the page is loaded for the first time.
  created() {
    this.getGames();
  },
};
</script>
