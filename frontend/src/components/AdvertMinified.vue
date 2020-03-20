<template>
    <div class="single-image m-2"  style="height: 25rem;">
      <div class="p-2">
        <router-link :to="{ name: 'ad_detail', params: { slug: advert.slug } }">
        <div class=" m-1 img ">
          
            <img
              :src="advert.file"
              style="height: 18rem; width: 12rem;"
              class="img-fluid "
              alt="Responsive image"
            />
        </div>
        

        <div class="mt-2 text-left pl-2">
          {{ advert.name }}
        </div>
        </router-link>

        <div class="mt-2 text-left pl-2">
            
              ₦{{ advert.price }}   
            
            <button 
                v-if="!isAdvertOwner"
                class="btn btn-sm"
                @click="toggle"

                :class="{
                    'btn-danger':  addedToWishList,
                    'btn-outline-danger':  !addedToWishList
                }"
            >
            <strong>add to wishlist</strong>
          </button>
        </div>
      </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js";


export default {
  name: "advert-detail-minified",

  props: {
    advert_object: {
      type: Object,
      required: true
    },

  },

  data() {
    return {
      advert: this.advert_object,
      requestUser: null,
      addedToWishList: this.advert_object.advert_in_current_user_wishlist
    };
  },

  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    
    toggle(){
      this.addedToWishList === false ? this.addTowishList() : this.removeFromWishList();
    },

    addTowishList(){
      
      let endpoint = `api/v1/user/wishlist/advert/${this.advert.slug}/`;
      apiService(endpoint, "POST");
      this.addedToWishList = true;
      
    },

    removeFromWishList(){
        
      let endpoint = `api/v1/user/wishlist/advert/${this.advert.slug}/`;
      apiService(endpoint, "DELETE");
      this.addedToWishList = false;
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
    
    this.setRequestUser();
  }
};
</script>

<style scoped>
  .single-image{
    background-color: #f9f9f9;
    font-size: 1.2rem;
  }

  .img{
    background-color: white;
    
  }
</style>
