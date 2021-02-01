<template>
  <div class=" p-0 mt-5">
    <router-link
      :to="{ name: 'ads_create', params: { slug: slug } }"
      class="btn btn-sm btn-success ml-2"
    >
      Edit Your Advert
    </router-link>

    <button @click="deleteAdvert" class="btn btn-sm ml-2 btn-danger">
      Delete Your Advert
    </button>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

export default {
  name: "advert-actions",

  props: {
    slug: {
      type: String,
      required: true
    }
  },

  data() {
    return {};
  },

  methods: {
    deleteAdvert(review) {
      let delete_advert_url = `api/v1/adverts/${this.slug}/`;

      apiService(delete_advert_url, "DELETE")
        .then(data => {
          this.$router.push("/adverts");
        })
        .catch(error => {
          console.log(error);
        });
    }
  }
};
</script>

<style scoped>
.btn{
    padding: 0.5rem;
    font-size: 1.2rem;
    letter-spacing: 0.1rem;
}

a{
    color: white!important;
}
</style>
