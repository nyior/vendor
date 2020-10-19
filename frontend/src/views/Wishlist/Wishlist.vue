<template>
  <div class=" container-fluid products">
    <Sell />

    <div
      v-if="adverts"
      class="row  pt-5 mt-5 categories  px-2 px-md-5 mt-0 mb-2 text-center d-flex"
    >
      <div class="col-md-3 col-6" v-for="advert in adverts" :key="advert.id">
        <AdvertMinified
          :advert_object="advert"
          @remove="removeFromWishList(advert.slug, advert)"
        />
      </div>
    </div>

    <div
      class="row p-5  mt-5 mb-2 text-center d-flex justify-content-center"
      v-if="noAdverts"
    >
      <div class="col-12 text-center">
        <h4 class="heading mt-4 mb-2 text-danger">
          <strong> You haven't saved any item yet !!</strong>
        </h4>

        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";
import { is_authenticated } from "@/common/global_variables.js";

import AdvertMinified from "@/components/Adverts/AdvertMinified.vue";

import Sell from "@/components/Others/Sell.vue";

export default {
  name: "wishlist",

  components: {
    AdvertMinified,
    Sell
  },

  data() {
    return {
      adverts: [],
      next: null,
      loadingAdverts: false,
      requestUser: null
    };
  },

  computed: {
    noAdverts() {
      if (this.adverts.length === 0) {
        return true;
      }
    }
  },

  methods: {
    getAdverts() {
      let get_adverts_url = "api/v1/user/wishlist/";

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

    removeFromWishList(slug, advert) {
      let endpoint = `api/v1/user/wishlist/advert/${slug}/`;
      apiService(endpoint, "DELETE");

      let index = this.adverts.indexOf(advert);
      this.adverts.splice(index, 1);
    },

    setRequestUser() {
      this.requestUser = window.localStorage.getItem("username");
    }
  },

  mounted: function() {
    this.setRequestUser();
    this.getAdverts();
    document.title = "Wishlist";
  },

  async beforeRouteEnter(to, from, next) {
    if (is_authenticated) {
      next();
    } else {
      next({
        name: "continue" // back to safety route //
      });
    }
  }
};
</script>

<style scoped></style>
