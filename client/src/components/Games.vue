<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Games</h1>
        <hr>
        <br><br>
        <alert :message="message" v-if="showMessage"></alert>
        <button type="button" class="btn btn-primary btn-sm" v-b-modal.game-modal>Add Game</button>
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
                <button
                  type="button"
                  class="btn btn-warning btn-sm"
                  @click="editGame(game)"
                  v-b-modal.game-update-modal>
                  Update
                </button>
                <button
                  type="button"
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
                        v-model="addGameForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-title-group"
                      label="Developer:"
                      label-for="form-developer-input">
          <b-form-input id="form-developer-input"
                        type="text"
                        v-model="addGameForm.developer"
                        required
                        placeholder="Enter developer">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addGameForm.favoured" id="form-checks">
            <b-form-checkbox value="false">Favoured?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Submit</b-button>
          <b-button type="reset" variant="danger">Reset</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
    <b-modal ref="editGameModal"
             id="game-update-modal"
             title="Update"
             hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-title-group"
                      label="Title:"
                      label-for="form-title-input">
          <b-form-input id="form-title-input"
                        type="text"
                        v-model="addGameForm.title"
                        required
                        placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-title-group"
                      label="Developer:"
                      label-for="form-developer-input">
          <b-form-input id="form-developer-input"
                        type="text"
                        v-model="addGameForm.developer"
                        required
                        placeholder="Enter developer">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addGameForm.favoured" id="form-checks">
            <b-form-checkbox value="false">Favoured?</b-form-checkbox>
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

export default {
  data() {
    return {
      games: [],
      addGameForm: {
        title: '',
        developer: '',
        favoured: [],
      },
      editForm: {
        id: '',
        title: '',
        developer: '',
        favoured: [],
      },
      message: '',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getGames() {
      const path = 'http://localhost:5000/games';
      axios.get(path)
        .then((res) => {
          this.games = res.data.games;
        })
        .catch((error) => {
          console.error(error);
        });
    },
    addGame(payload) {
      const path = 'http://localhost:5000/games';
      axios.post(path, payload)
        .then(() => {
          this.getGames();
          this.message = 'Game added!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getGames();
        });
    },
    initForm() {
      this.addGameForm.title = '';
      this.addGameForm.developer = '';
      this.addGameForm.favoured = [];
      this.editForm.id = '';
      this.editForm.title = '';
      this.editForm.developer = '';
      this.editForm.favoured = [];
    },
    onsubmit(evt) {
      evt.preventDefault();
      this.$refs.addGameModal.hide();

      let favoured = false;

      if (this.addGameForm.favoured[0]) favoured = true;

      const payload = {
        title: this.addGameForm.title,
        developer: this.addGameForm.developer,
        favoured,
      };

      this.addGame(payload);
      this.initForm();
    },
    onreset(evt) {
      evt.preventDefault();
      this.$refs.addGameModal.hide();
      this.initForm();
    },
    onSubmitUpdate(evt) {
      evt.preventDefault();
      this.$refs.editGameModal.hide();

      let favoured = false;

      if (this.editForm.read[0]) favoured = true;

      const payload = {
        title: this.editForm.title,
        developer: this.editForm.developer,
        favoured,
      };

      this.updateGame(payload, this.editForm.id);
    },
    updateGame(payload, gameId) {
      const path = `http://localhost:5000/games/${gameId}`;
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
    onResetUpdate(evt) {
      evt.preventDefault();
      this.$refs.editGameModal.hide();
      this.initForm();
      this.getGames();
    },
    removeGame(gameID) {
      const path = `http://localhost:5000/games/${gameID}`;

      axios.delete(path)
        .then(() => {
          this.getGames();
          this.message = 'Game removed!';
          this.showMessage = true;
        })
        .catch((error) => {
          console.log(error);
          this.getGames();
        });
    },
    onDeleteGame(game) {
      this.removeGame(game);
    },
    editGame(game) {
      this.editForm = game;
    },
  },
  created() {
    this.getGames();
  },
};
</script>
