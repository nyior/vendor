<template>
  <div class=" container advert mt-5 ">
    <div class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center">
      
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
            <div class="text-muted mt-2">
              <p>
                <a href="#">
                  <strong>
                    {{ advert.name }} <br />
                    {{ advert.price }}
                  </strong>
                </a>
              </p>

              <hr>
              <router-link
                  :to ="{name: 'user_detail', params:{id: advert.user.id}}">
                  Seller: {{ advert.user.username }}

              </router-link>
            </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>

import {apiService } from "../common/api.service.js";

export default {
  name: "advert-detail",

  props: {
      slug: {
          type: String,
          required: true
      }
  },
  data() {
    return {
      advert: null
    };
  },

  methods: {

    setPageTitle(title){
        document.title = title;
    },

    getAdvert() {
     let get_adverts_url = `api/v1/adverts/${this.slug}/`;

     apiService(get_adverts_url, 'GET')
          .then(data => {
              this.advert=data
              this.setPageTitle(data.name)
          })
    }
  },

  mounted: function() {
    this.getAdvert();
  }
};
</script>

<style scoped>

</style>
