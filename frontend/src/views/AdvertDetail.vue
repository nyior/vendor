<template>

  <div class=" container advert mt-5 ">
    <router-link class="sell" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>
    <div
      class="row   pt-5 mt-5 mb-2 text-center d-flex justify-content-center align-items-center"
    >
      <div class="col-md-3 col-6 p-0">

          <AdvertMinified :advert_object="advert"/>
        
          <advertActions v-if="isAdvertOwner"
                          :slug="advert.slug"
                          :category="advert.category"/>
          
            <hr />
          <router-link
              :to="{ name: 'user_detail', params: { id: advert.user.id } }"
          >
            Seller: {{ advert.user.username }}
          </router-link>
      </div>
    </div>
  </div>

</template>

<script>
  import { apiService } from "../common/api.service.js";
  import advertActions from "@/components/advertActions.vue"
  import AdvertMinified from "@/components/AdvertMinified.vue";

  export default {
    name: "advert-detail",

    components: {
      advertActions,
      AdvertMinified
    },

    props: {
      slug: {
        type: String,
        required: true
      },

    },

    data() {
      return {
        advert: null,
        requestUser: null,
        addedToWishList: null,
        counter: 0,
        message: null
      };
    },

    methods: {
      setPageTitle(title) {
        document.title = title;
      },

      getAdvert() {
        let get_adverts_url = `api/v1/adverts/${this.slug}/`;

        apiService(get_adverts_url, "GET").then(data => {
          this.advert = data;
          this.addedToWishList = data.advert_in_current_user_wishlist;
          this.setPageTitle(data.name);

        });
      },
      toggle(){
        this.addedToWishList === false ? this.addTowishList() : this.removeFromWishList();
      },

      addTowishList(){
        
        let endpoint = `api/v1/user/wishlist/advert/${this.slug}/`;
        apiService(endpoint, "POST");
        this.addedToWishList = true;
        this.counter += 1;
        this.message = "advert added to your wishlist"
      },

      removeFromWishList(){
          
        let endpoint = `api/v1/user/wishlist/advert/${this.slug}/`;
        apiService(endpoint, "DELETE");
        this.addedToWishList = false;

        this.counter -= 1
        this.message = "advert removed from your wishlist"
      },

      setRequestUser(){
          this.requestUser = window.localStorage.getItem("username");
      }
    },

    computed: {
        isAdvertOwner(){
            return this.advert.user.username === this.requestUser;
        }
    },


    mounted: function() {
      this.getAdvert();
      this.setRequestUser();
    }
  };
  
</script>

<style scoped></style>
