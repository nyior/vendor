<template>
  <div class=" container mt-5">
    <div
      class="row pt-5 mt-5"
    >
        <div class="col-md-4 col-12 p-0  ml-md-auto px-5 py-3">
            <div>
                <img
                    :src="advert.file"
                    class="img-fluid"
                    :alt="advert.name + ' image'"
                />
            </div>
            
            <advertActions
                v-if="isAdvertOwner"
                :slug="advert.slug"
                :category="advert.category"
            />
            <div
                v-else
                class="mt-3"
            >
            <span>
                <a 
                 :href="mailTo"
                >
                    email seller
                </a> 
            </span>
            </div>
            
        </div>

        <div class="col-md-6 mr-md-auto px-5 py-3 mt-md-0 mt-5">
            <span>
                uploaded by 
                <router-link
                    :to="{ name: 'user_detail', params: { id: advert.user.id } }"
                >
                    {{ advert.user.username }}
                </router-link>
            </span>

            <div class="mt-3">
                <p id="productName">
                    {{ advert.name }}
                </p>
            </div>

            <hr>

            <div>
                <p id="price">
                    ₦{{ advert.price }}
                </p>
            </div>

            <hr>

            <div>
                <p id="description">
                    {{ advert.description}}
                </p>
                <div>
                    <button 
                        class="blue-btn btn-block" 
                        type="submit"
                        
                        @click="toggle"
                        >
                        <div v-if="!addedToWishList">
                            <span class="wishlist-cta">
                                <i class="fa fa-gratipay"></i>
                            </span>
                            <span 
                                class="wishlist-cta" 
                            >
                                add to wishlist
                            </span>
                        </div>
                        
                        <div v-else>
                            <span class="wishlist-cta">
                                <i class="fa fa-trash-o" aria-hidden="true"></i>
                            </span>
                            <span 
                            class="wishlist-cta" 
                            
                            >
                                remove from wishlist
                            </span>
                        </div>
                        
                    </button>
                </div>
            </div>

        </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { store } from "@/store/store";

// I will have to figure out how to import multiple files at once
import AdvertActions from "@/components/Adverts/AdvertActions.vue";

export default {
  name: "advert-detail",

  components: {
    AdvertActions
  },

  props: {
    slug: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      advert: null,
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
    toggle() {
      this.addedToWishList === false
        ? this.addTowishList()
        : this.removeFromWishList();
    },

    addTowishList() {
      let endpoint = `api/v1/user/wishlist/advert/${this.slug}/`;
      apiService(endpoint, "POST");
      this.addedToWishList = true;
      this.counter += 1;
      this.message = "advert added to your wishlist";
    },

    removeFromWishList() {
      let endpoint = `api/v1/user/wishlist/advert/${this.slug}/`;
      apiService(endpoint, "DELETE");
      this.addedToWishList = false;

      this.counter -= 1;
      this.message = "advert removed from your wishlist";
    }
  },

  computed: {
    isAdvertOwner() {
      let username = this.$store.state.username;
      return this.advert.user.username === username;
    },

    mailTo() {
        return `mailto:${this.advert.user.username}?subject=${this.advert.name} purchase`
    }
  },

  mounted: function() {
    this.getAdvert();
  },

  async beforeRouteEnter(to, from, next) {
    let isAuth = store.state.isAuthenticated;
    if (isAuth === true) {
      next();
    } else {
      next({
        name: "continue" // back to safety route //
      });
    }
  }
};
</script>

<style scoped>
span{
    background-color: #7a09c4;
    color: white;
    font-weight: bold;
    font-size: 1.2rem;
    padding: 0.3rem;
    border-radius: 0.3rem;
}

#productName{
    font-size: 4.0rem;
}

#price{
    font-size: 3rem;
    font-weight: 400;
    letter-spacing: 0.1rem;
}

a{
    color: #e00029 !important;
    font-weight: bold;
}

#description{
    font-size: 1.4rem;
    letter-spacing: 0.1rem;
}

.fa{
    color: white !important;
}

.wishlist-cta{
    font-size: 1.6rem;
    letter-spacing: 0.1rem;
}
</style>
