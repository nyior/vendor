<template>
  <div class="container-fluid pt-5 pb-0 mt-5  ">
    <router-link class="sell hide-on-mobile" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>

    <div class="row  text-center px-4 hide-on-desktop">

      <div class="col-md-12">

        <form class="form-group has-search py-3"
                @submit.prevent="onSubmit">
          <input
              class="form-control mr-sm-2 p-3 px-4"
              type="search"
              placeholder="Search and discover products/services on Marche"
              required
              v-model="search_word"
          />
        </form>

      </div>

    </div>
    
    <div class="row categories px-2 px-md-5 mt-0 mb-2 text-center d-flex">
      <div class="col-md-3 col-6" v-for="advert in adverts" :key="advert.id">
        <AdvertMinified :advert_object="advert" />
      </div>
    </div>

    <div class="row text-center d-flex justify-content-center mt-4">
      <div class="col-6">
        <p v-show="loadingAdverts">...loading...</p>
        <a v-show="next" @click="getSearchResults" class>
          <strong>Load More</strong>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import AdvertMinified from "@/components/AdvertMinified.vue";

export default {
  name: "SearchView",

  props: {
	  search_key: {
		  type: String,
		  required: false,
	  }
  },

  data() {
    return {
      adverts: [],
      next: null,
      loadingAdverts: false,
	    search_word: this.search_key
    };
  },

  components: {
    AdvertMinified
  },

  methods: {
    getSearchResults() {
      let get_adverts_url = "api/v1/adverts/";

      if (this.next) {
        get_adverts_url = this.next.slice(22);
      }

      this.loadingAdverts = true;
      apiService(get_adverts_url, "GET").then(data => {
        this.loadingAdverts = false;
        this.adverts.push(...data.results);

        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },

  },

  mounted: function() {
    this.getSearchResults();
    document.title = "Search Results";
  }
};
</script>

<style scoped>
  
</style>
