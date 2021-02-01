<template>
  <div class="container-fluid pt-5 pb-0 mt-5  ">
    <Sell />

    <div class="row px-3 hide-on-desktop">
        <div class="col-12">
            <SearchForm />
        </div>
        
    </div>

    <div class="row px-3 text-center mb-5" v-if="loadingAdverts">
      <div class="col-md-6 ml-md-auto mr-md-auto col-12">
        <Loader />
      </div>
    </div>

    <div 
        class="row categories px-3 mt-5 mb-2 text-center " 
        v-if="!noAdverts"
    >
      <div 
        class="col-md-3 col-12" 
        v-for="advert in adverts" 
        :key="advert.id">
        <AdvertMinified :advert_object="advert" />
      </div>
    </div>

    <div
      class="row p-5  mt-5 mb-2 text-center d-flex justify-content-center"
      v-else
    >
      <div class="col-12 text-center">
        <h4 class="heading mt-4 mb-2 text-danger">
          <strong> no items found</strong>
        </h4>
      </div>
    </div>

    <div class="row text-center d-flex justify-content-center mt-5">
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
import { apiService } from "@/common/api.service.js";
import AdvertMinified from "@/components/Adverts/AdvertMinified.vue";
import Sell from "@/components/Others/Sell.vue";
import SearchForm from "@/components/Search/SearchForm.vue";
import Loader from "@/components/Utils/Loader.vue";

export default {
  name: "SearchView",

  components: {
    SearchForm,
    AdvertMinified,
    Sell,
    Loader
  },

  props: {
    search_key: {
      type: String,
      required: false
    }
  },

  data() {
    return {
      adverts: [],
      users: [],
      next: null,
      loadingAdverts: false,
      search_word: this.search_key
    };
  },

  methods: {
    getSearchResults() {
      let search_url = `api/v1/search/?search=${this.search_word}`;

      if (this.next) {
        search_url = this.next.slice(22);
      }

      this.loadingAdverts = true;
      apiService(search_url, "GET").then(data => {
        this.loadingAdverts = false;
        this.adverts = [...data["adverts"]];
        this.users = [...data["users"]];

        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    }
  },

  computed: {
    noAdverts() {
      if (this.adverts.length === 0) {
        return true;
      }
    }
  },

  mounted: function() {
    this.getSearchResults();
    document.title = "Search Results";
  },

  beforeRouteUpdate (to, from, next) {
    this.search_word = to.params.search_key;
    this.getSearchResults();;
    next();
  }
};
</script>

<style scoped>
</style>
