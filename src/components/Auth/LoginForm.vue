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
            <small>
              <router-link class="text-muted" :to="{ name: 'register' }">
                don't have an account? register
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
  name: "login-form",

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
      text: "login",
      form: {
        username: null,
        password: null
      }
    };
  },

  methods: {
    onSubmit() {
      this.$emit('login', this.form);
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
