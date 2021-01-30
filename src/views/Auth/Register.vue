<template>
  <div class="container">
    <div class="row d-flex  justify-content-center align-items-center px-5">
      <div class="col-12 text-center ">
        <h1 class="heading mt-5 mb-2">
          Create an Account
        </h1>
      </div>

      <div class="col-md-6 col-12 mt-5 shadow border px-3 py-3">
        <form
          @submit.prevent="createUser"
          class="p-3 was-validated"
          enctype="multipart/form-data"
        >
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              placeholder="valid AUN email here"
              required
              v-model="form.email"
            />
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

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

          <div class="form-group mt-3">
            <input
              type="password"
              class="form-control"
              placeholder="confirm your password here"
              required
              v-model="confirmPassword"
            />
            <div class="invalid-feedback">
              Please fill out this field
            </div>
          </div>

          <button class="blue-btn btn-block" type="submit">
            register
          </button>
        </form>

        <div class="p-3">
          <p v-if="error" class="mt-2">
            <strong>{{ error }}</strong>
          </p>

          <span>
            <small class="color-purple">
              <router-link :to="{ name: 'login' }" class="text-muted">
                already have an account? Login
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
      confirmPassword: null,
      form: {
        email: null,
        username: null,
        password: null
      }
    };
  },

  methods: {
    createUser() {
      let create_user_url = `api/v1/user/signup/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("email", this.form.email);
      formData.append("username", this.form.username);
      formData.append("password", this.form.password);

      apiService(create_user_url, method, formData)
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
    document.title = "Register";
  }
};
</script>

<style scoped></style>
