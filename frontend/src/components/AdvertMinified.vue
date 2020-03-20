<template>
    <div>
        <router-link :to="{ name: 'ad_detail', params: { slug: advert.slug } }">
        <div class=" m-1 bg-grey mt-5">
          
            <img
              :src="advert.file"
              style="height: 18rem;"
              class="img-fluid m-1"
              alt="Responsive image"
            />
        </div>
        

        <div class="text-muted mt-2">
            <p>
              <a href="#">
                <strong>
                  {{ advert.name }} <br />
                  {{ advert.price }}
                </strong>
              </a>
            </p>

        </div>
        </router-link>

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

<style scoped></style>
