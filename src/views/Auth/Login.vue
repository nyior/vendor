<template>
  <div class="container">

    <div class="row d-flex  justify-content-center align-items-center px-5">
      <div class="col-12 text-center ">
        <h1 class="heading mt-5 mb-2">
          Login to Your Account
        </h1>
      </div>
    </div>

    <LoginForm 
        :error="error" 
        :isLoading="isLoading"
        @login="login"
    />

  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import LoaderButton from "@/components/Utils/LoaderButton.vue";
import LoginForm from "@/components/Auth/LoginForm.vue";

export default {
  name: "login",

  components: {
    LoaderButton,
    LoginForm
  },

  data() {
    return {
      error: null,
      isLoading: false
    };
  },

  methods: {
    login(form) {
      this.isLoading = true;
      let login_url = `api/v1/user/login/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("username", form.username);
      formData.append("password", form.password);

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

<style scoped>
span{
    color: red !important;
    margin-top: 0.2rem;
    font-size: 1.2rem;
}
</style>
