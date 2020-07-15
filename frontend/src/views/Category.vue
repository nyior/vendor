<template>
  <div class=" container-fluid products">
    <router-link class="sell" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>
    <div class="row p-5  mt-5 mb-2 text-center d-flex justify-content-center">
        <div class="col-12 ">
             <CategoriesList/>
        </div>
    </div>

    <div
      v-if="adverts"
      class="row  categories   px-2 px-md-5 mt-0 mb-2 text-center d-flex"
    >
    <div
        class="col-md-3 col-6 "
        v-for="advert in adverts"
        :key="advert.id"
    >
      <AdvertMinified :advert_object="advert"/>
    </div>
    <div class="row p-5  mt-5 mb-2 text-center d-flex justify-content-center" v-if="noAdverts">
        <div class="col-12 text-center">
             <h4 class="heading mt-4 mb-2 text-danger">
                 <strong> Nothing found in this category, may be check back later !!</strong>
            </h4>
        </div>
    </div>
    </div>

    <div class="row text-center d-flex justify-content-center mt-4">
      <div class="col-6">
        <p v-show="loadingAdverts">...loading...</p>
        <a v-show="next" @click="getAdverts" class=" ">
          <strong> Load More</strong>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import CategoriesList from "@/components/CategoriesList.vue";
import AdvertMinified from "@/components/AdvertMinified.vue";

export default {
  name: "adverts-category",
  
  components: {
      CategoriesList,
      AdvertMinified
  },

  props: {
      category: {
          type: String,
          required: true
      }
  },

  data() {
    return {
      adverts: [],
      next: null,
      loadingAdverts: false,
      requestUser: null,
      advert_category: this.category
    };
  },

  computed: {
      noAdverts(){
          if(this.adverts.length === 0){
              return true;
          }
      }
  },
  
  methods: {
    getAdverts() {
      let get_adverts_url = `api/v1/${this.advert_category}/adverts/`;

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

    setRequestUser(){
        this.requestUser = window.localStorage.getItem("username");
    }
  },

  mounted: function() {
    this.setRequestUser();
    
  },
  created(){
    this.getAdverts();
    document.title = "Advertisements";
   }
};
</script>

<style scoped>
.home-hero {
  font-size: 1.4rem;
  background-image: linear-gradient(#7a09c4, #200135);
  color: white;
}
</style>
