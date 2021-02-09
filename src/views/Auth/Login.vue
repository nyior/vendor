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
          class="p-3"
          enctype="multipart/form-data"
        >
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              v-validate="'required|alpha_num|alpha_dash'"
              name="username"
              required
              placeholder="your username here"
              v-model="form.username"
            />
            <div class="mt-2">
                <span>{{ errors.first('username') }}</span>
            </div>
          </div>

          <div class="form-group mt-3">
            <input
              type="password"
              class="form-control"
              placeholder="your password here"
              v-validate="'required|min:8'"
              name="password"
              required
              v-model="form.password"
            />
            <div class="mt-2">
                <span>{{ errors.first('password') }}</span>
            </div>
          </div>

          <!-- <button class="blue-btn btn-block" type="submit">
            login
          </button> -->

          <LoaderButton 
                :status="isLoading" 
                :text="text"
          />
        </form>

        <div class="p-3">
          <p v-if="error" class="mt-2 text-danger">
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
import LoaderButton from "@/components/Utils/LoaderButton.vue";

export default {
  name: "login",

  components: {
    LoaderButton
  },

  data() {
    return {
      error: null,
      isLoading: false,
      form: {
        username: null,
        password: null
      }
    };
  },

  computed: {
      text(){
          return "login"
      }
  },

  methods: {
    login() {
      this.isLoading = true;
      let login_url = `api/v1/user/login/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("username", this.form.username);
      formData.append("password", this.form.password);

      apiService(login_url, method, formData)
        .then(data => {
          let payload = {
            authToken: data.token,
            userId: data.id,
            username: data.username
          };

          this.$store.dispatch("joinAction", payload);
          
          this.isLoading = false;

          this.$router.push({
            name: "home"
          });
        })
        .catch(error => {
          this.isLoading = false;
          this.error = "invalid credentials";
        });
    }
  },

  mounted: function() {
    document.title = "Login";
  }
};
</script>

<style scoped></style>
