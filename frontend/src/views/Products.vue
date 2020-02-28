<template>
  <div class="products">
    <div
      class="row  categories  p-5  mt-4 mb-2 text-center d-flex justify-content-center"
    >
      <div class="col-md-3 col-6 p-0">
        <div class="card m-2">
          <div class="mt-5">
            <a href="#"><i class="fa fa-shirtsinbulk"></i></a>
          </div>
          <hr />
          <div class="card-body text-muted">
            <a href="#"><strong>FASHION</strong></a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { APIService } from "../common/api.service.js";
const apiservice = new APIService();

//requests endpoints
const get_products_url = "api/v1/products/";

export default {
  name: "products",
  data() {
    return {
      products: null
    };
  },

  methods: {
    getProducts() {
      apiservice
        .getResource(get_products_url)
        .then(data => (this.products = data))
        .catch(error => console.log(error));
    }
  },

  mounted: function() {
    this.getProducts();
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
