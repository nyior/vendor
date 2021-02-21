<template>
  <div class=" container">

    <div
      class="row p-5 mt-5  mb-2 text-left d-flex  justify-content-center align-items-center"
    >
      <div class="col-12 text-center ">
        <h1 class="heading mt-5 mb-2">
          Create an Advert
        </h1>
      </div>
    </div>

    <AdvertForm
        :error="error"
        :isLoading="isLoading"
        :responseData="responseData"
    />
    
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import { store } from "@/store/store";

import JoinMarche from "@/components/Modals/JoinMarche.vue";

import LoaderButton from "@/components/Utils/LoaderButton.vue";
import AdvertForm from "@/components/Adverts/AdvertForm.vue"

export default {
  name: "adverts-create",

  components: {
    JoinMarche,
    LoaderButton,
    AdvertForm
  },

  props: {
    slug: {
      type: String,
      required: false
    },

    responseData: {
      type: Object,
      required: false
    }
  },

  data() {
    return {
      error: null,
      isLoading: false,
    };
  },

  methods: {

    postAdvert(form) {
      this.isLoading = true;
      let post_advert_url = `api/v1/adverts/`;

      let method = "POST";
      let file = this.form.file;
      let formData = new FormData();

      if (this.slug !== undefined) {
        post_advert_url = `api/v1/adverts/${this.slug}/`;
        method = "PUT";
      }

      formData.append("category", form.category);
      formData.append("name", form.name);
      formData.append("price", form.price);
      formData.append("file", file);

      if (
          this.form.quantity !== undefined && this.form.quantity !== null
          ) {
        formData.append("quantity", this.form.quantity);
      }

      if (
          this.form.description !== undefined && this.form.description !== null
        ) {
        formData.append("description", this.form.description);
      }

      apiService(post_advert_url, method, formData)
        .then(data => {
          this.isLoading = false;
          this.$router.push({
            name: "ad_detail",
            params: { slug: data.slug }
          });
        })
        .catch(error => {
          this.isLoading = false;
          this.error = "something wrong with your request";
        });
    }
  },

  async beforeRouteEnter(to, from, next) {
    let isAuth = store.state.isAuthenticated;

    if (to.params.slug !== undefined && isAuth === true) {
      let get_advert_url = `api/v1/adverts/${to.params.slug}/`;

      let data = await apiService(get_advert_url, "GET");
      to.params.responseData = data;

      return next();
    } else if (isAuth === true) {
        return next();
    } else {
      return next({
        name: "continue" // back to safety route //
      });
    }
  },

  mounted: function() {
    document.title = "Create Advert";
  }
};
</script>

<style scoped>
p {
  z-index: 1;
}
</style>
