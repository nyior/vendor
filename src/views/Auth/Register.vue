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
          class="p-3"
          enctype="multipart/form-data"
        >
          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              placeholder="valid email here"
              v-validate="'required|email'"
              name="email"
              required
              v-model="form.email"
            />
            <div class="mt-2">
                <span>{{ errors.first('email') }}</span>
            </div>
          </div>

          <div class="form-group mt-3">
            <input
              type="text"
              class="form-control"
              placeholder="phone number here"
              v-validate="'required|digits'"
              name="phone"
              required
              v-model="form.phoneNumber"
            />
            <div class="mt-2">
                <span>{{ errors.first('phone') }}</span>
            </div>
          </div>


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

          <!-- <div class="form-group mt-3">
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
          </div> -->

          <LoaderButton 
                :status="isLoading" 
                :text="text"
          />

          <!-- <button class="blue-btn btn-block" type="submit">
            register
          </button> -->
        </form>

        <div class="p-3">
          <p v-if="error" class="mt-2 text-danger">
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
import LoaderButton from "@/components/Utils/LoaderButton.vue";

export default {
  name: "register",

  components: {
    LoaderButton
  },

  data() {
    return {
      error: null,
      isLoading: false,
      confirmPassword: null,
      form: {
        email: null,
        username: null,
        password: null,
        phoneNumber: null,
      }
    };
  },

  computed: {
      text(){
          return "register"
      }
  },

  methods: {
    createUser() {
      this.isLoading = true;
      let create_user_url = `api/v1/user/signup/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("email", this.form.email);
      formData.append("username", this.form.username);
      formData.append("password", this.form.password);
      formData.append("phone_number", this.form.phoneNumber);

      apiService(create_user_url, method, formData)
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
          this.error = "something wrong with the data you provided";
        });
    }
  },

  mounted: function() {
    document.title = "Register";
  }
};
</script>

<style scoped></style>
