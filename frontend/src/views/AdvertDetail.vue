<template>
  <div class=" container advert mt-5 ">
    <div
      class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center"
    >
      <div class="col-md-4 col-6 p-0">
        <div class=" m-1 bg-grey mt-5">
          <a :href="advert.file">
            <img
              :src="advert.file"
              style="height: 18rem;"
              class="img-fluid m-1"
              alt="Responsive image"
            />
          </a>

          <advertActions v-if="isAdvertOwner"
                          :slug="advert.slug"
                          :category="advert.category"/>

          <div class="text-muted mt-2">
            <p>
              <a href="#">
                <strong>
                  {{ advert.name }} <br />
                  {{ advert.price }}
                </strong>
              </a>
            </p>

            <hr />
            <router-link
              :to="{ name: 'user_detail', params: { id: advert.user.id } }"
            >
              Seller: {{ advert.user.username }}
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import advertActions from "@/components/advertActions.vue"

export default {
  name: "advert-detail",

  components: {
    advertActions
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
        this.setPageTitle(data.name);
      });
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
