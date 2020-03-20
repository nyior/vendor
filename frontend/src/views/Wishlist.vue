<template>
  <div class=" container products">
    <div
      v-if="adverts"
      class="row  categories  p-5  mt-5 mb-2 text-center d-flex justify-content-center"
    >
      <div
        class="col-md-2 col-6 p-0"
        v-for="advert in adverts"
        :key="advert.id"
      >
        <router-link :to="{ name: 'ad_detail', params: { slug: advert.slug } }">
          <div class=" m-1 bg-grey">
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
            </div>

          </div>
        </router-link>
        <button class="btn  btn-danger btn-sm" @click="removeFromWishList(advert.slug, advert)"> delete</button>
      </div>
    </div>

    <div class="row p-5  mt-5 mb-2 text-center d-flex justify-content-center" v-if="noAdverts">
        <div class="col-12 text-center">
             <h4 class="heading mt-4 mb-2 text-danger">
                 <strong> You haven't saved any item yet !!</strong>
            </h4>
        </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "wishlist",
  data() {
    return {
      adverts: [],
      next: null,
      loadingAdverts: false,
      requestUser: null
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

    removeFromWishList(slug, advert){
        
      let endpoint = `api/v1/user/wishlist/advert/${slug}/`;
      apiService(endpoint, "DELETE");

      let index = this.adverts.indexOf(advert);
      this.adverts.splice(index, 1);
    
    },

    setRequestUser(){
        this.requestUser = window.localStorage.getItem("username");
    }
  },

  mounted: function() {
    this.setRequestUser();
    this.getAdverts();
    document.title = "Wishlist";  
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
