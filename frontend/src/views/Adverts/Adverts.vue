<template>
  <div class="container-fluid products">
    <router-link class="sell" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>
    <div class="row pt-5 pb-0 mt-5 mb-2 text-center d-flex justify-content-center">
      <div class="col-12">
        <CategoriesList />
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
        <a v-show="next" @click="getAdverts" class>
          <strong>Load More</strong>
        </a>
      </div>
    </div>
  </div>
</template>

<script>

  import { apiService } from "@/common/api.service.js";
  
  import CategoriesList from "@/components/Category/CategoriesList.vue";
  import AdvertMinified from "@/components/Adverts/AdvertMinified.vue";

  export default {
    name: "adverts",
    data() {
      return {
        adverts: [],
        next: null,
        loadingAdverts: false,
        requestUser: null,
        addedToWishList: null
      };
    },

    components: {
      CategoriesList,
      AdvertMinified
    },

    methods: {
      getAdverts() {
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

      setRequestUser() {
        this.requestUser = window.localStorage.getItem("username");
      }
    },

    mounted: function() {
      this.setRequestUser();
    },
    created() {
      this.getAdverts();
      document.title = "Advertisements";
    }
  };

</script>

<style>

  .sell {
    position: fixed;
    bottom: 50px;
    right: 50px;
    z-index: 10;
  }

  .sell button{
    background: #f0f0f0!important;
    font-size: 1.5rem;
    padding: 1rem 1.2rem;
  }

  @media only screen and (max-width: 600px) {
    
    .sell {
      position: fixed;
      bottom: 30px;
      right: 20px;
    }
  }
  
</style>
