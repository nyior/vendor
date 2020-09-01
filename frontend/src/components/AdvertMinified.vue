<template>

  <div style="position: relative">

    <router-link :to="{ name: 'ad_detail', params: { slug: advert.slug } }">

      <div class="m-1 bg-grey mt-5">
        <div id="productImageBackground">
          <img :src="advert.file" class="img-fluid productImage" alt="Responsive image" />
        </div>
      </div>

      <div class="text-muted mt-2">

        <div class="d-flex" id="productText">
          <p id="productName">{{ advert.name }}</p>
          <p id="price ml-md-auto">₦{{ advert.price }}</p>
        </div>
         
      </div>

    </router-link>

    <button v-if="!isAdvertOwner" class="btn btn-sm" @click="toggle" id="wishlist">
      <i class="far fa-heart fa-3x" v-if="!addedToWishList"></i>
      <i class="fas fa-heart fa-3x" v-else></i>
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
      }
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

      toggle() {
        this.addedToWishList === false
          ? this.addTowishList()
          : this.removeFromWishList();
      },

      addTowishList() {
        let endpoint = `api/v1/user/wishlist/advert/${this.advert.slug}/`;
        apiService(endpoint, "POST");
        this.addedToWishList = true;
      },

      removeFromWishList() {
        let endpoint = `api/v1/user/wishlist/advert/${this.advert.slug}/`;
        apiService(endpoint, "DELETE");
        this.addedToWishList = false;
        this.$emit("remove");
      },

      setRequestUser() {
        this.requestUser = window.localStorage.getItem("username");
      }
    },

    computed: {
      isAdvertOwner() {
        return this.advert.user.username === this.requestUser;
      }
    },

    mounted: function() {
      this.setRequestUser();
    }
  };

</script>


<style scoped>

  #price {
    font-weight: 600;
    font-size: 1.3rem;
  }

  #productText {
    flex-flow: row;
  }

  #productName {
    font-size: 1.3rem;
  }

  #productImageBackground {
    height: 300px;
    overflow: hidden;
    display: flex;
    justify-content: center;
    flex-flow: column;
  }

  #wishlist{
    position: absolute;
    top: 0;
    right: 0;
    background: white;
    padding: 1.7rem;
    border-bottom-left-radius: 10px;
  }

  #wishlist i{
    color: #7A09C4;
    outline: none!important;
    box-shadow: none!important;
  }

  a:hover {
    color: rgba(0, 0, 0, 0.8) !important;
  }


  @media only screen and (max-width: 640px) {
    #productText {
      flex-flow: column;
    }

    #productName {
      font-size: 1rem;
    }

    #price {
      font-size: 1rem;
    }
  }

</style>
