<template>
  <div class="container">
    <div class="row d-flex  justify-content-center align-items-center px-5">
      <div class="col-12 text-center ">
        <h1 class="heading mt-5 mb-2">
          Login to Your Account
        </h1>
      </div>

      <div class="col-md-6 col-12 mt-5 shadow border px-3 py-3">
        <form
          @submit.prevent="login"
          class="p-3 was-validated"
          enctype="multipart/form-data"
        >
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              required
              placeholder="your username here"
              v-model="form.username"
            />
            <div class="invalid-feedback">Please fill out this field</div>
          </div>

          <div class="form-group mt-3">
            <input
              type="password"
              class="form-control"
              placeholder="your password here"
              required
              v-model="form.password"
            />
            <div class="invalid-feedback">
              Please fill out this field
            </div>
          </div>

          <button class="btn  blue-btn btn-block" type="submit">
            login
          </button>
        </form>

        <div class="p-3">
          <p v-if="error" class="mt-2">
            <strong>{{ error }}</strong>
          </p>

          <span>
            <small>
              <router-link class="text-muted" :to="{ name: 'register' }">
                don't have an account? register
              </router-link>
            </small>
          </span>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "register",

  data() {
    return {
      error: null,
      form: {
        username: null,
        password: null
      }
    };
  },

  methods: {
    login() {
      let login_url = `api/v1/user/login/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("username", this.form.username);
      formData.append("password", this.form.password);

      apiService(login_url, method, formData)
        .then(data => {
          let payload = {
            authToken: data.token,
            userId: data.id
          };

          this.$store.dispatch("joinAction", payload);

          this.$router.push({
            name: "home"
          });
        })
        .catch(error => {
          this.error = error;
        });
    }
  },

  mounted: function() {
    document.title = "Login";
  }
};
</script>

<style scoped></style>
