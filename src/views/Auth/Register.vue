<template>
  <div class="container">

      <div class="row d-flex  justify-content-center align-items-center px-5">
        <div class="col-12 text-center ">
            <h1 class="heading mt-5 mb-2">
                Create an Account
            </h1>
        </div>
      </div>

      <SignUpForm 
            :error="error" 
            :isLoading="isLoading"
            @submit="createUser"
      />

  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import LoaderButton from "@/components/Utils/LoaderButton.vue";
import SignUpForm from "@/components/Auth/SignUpForm.vue";

export default {
  name: "register",

  components: {
    LoaderButton,
    SignUpForm
  },

  data() {
    return {
      error: null,
      isLoading: false
    };
  },

  methods: {
    createUser(form) {
      this.isLoading = true;
      let create_user_url = `api/v1/user/signup/`;

      let method = "POST";
      let formData = new FormData();

      formData.append("email", form.email);
      formData.append("username", form.username);
      formData.append("password", form.password);
      formData.append("phone_number", form.phoneNumber);

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

<style scoped>
span{
    color: red !important;
    margin-top: 0.2rem;
    font-size: 1.2rem;
}
</style>
