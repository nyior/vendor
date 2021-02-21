<template>
    <div class="row d-flex  justify-content-center align-items-center px-5">
      <div class="col-md-6 col-12 mt-5 shadow border px-3 py-3">
        <form
          @submit.prevent="onSubmit"
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
            <small class="color-purple">
              <router-link :to="{ name: 'login' }" class="text-muted">
                already have an account? Login
              </router-link>
            </small>
          </span>
        </div>
      </div>
    </div>
</template>

<script>
import LoaderButton from "@/components/Utils/LoaderButton.vue";

export default {
  name: "signup-form",

  components: {
    LoaderButton
  },

  props: {
      error: {
          type: String,
          required: true
      },

      isLoading: {
          type: Boolean,
          required: true
      }
  },

  data() {
    return {
      text: "register",
      form: {
        email: null,
        username: null,
        password: null,
        phoneNumber: null,
      }
    };
  },

  methods: {
    onSubmit() {
      this.$emit('submit', this.form);
    }
  },

};
</script>

<style scoped>
span{
    color: red !important;
    margin-top: 0.2rem;
    font-size: 1.2rem;
}
</style>
