<template>
  <div class=" container products">
    <div class="row  categories  p-5 mt-5  mb-2 text-left d-flex justify-content-center align-items-center">
      
      <div class="col-md-6 col-12 mt-5 shadow border">
        <h1 class="heading mt-4 mb-2">
          Create an Advert Now
        </h1>

        <form 
         @submit.prevent="postAdvert" class="p-3 was-validated"  enctype="multipart/form-data">

            <div class="form-group">
                <label for="advert-name">Advert Name</label>
                <input type="text" class="form-control" id="advert-name" placeholder="example: Iphone 5 64GB Gold" required v-model="form.name">
                <div class="invalid-feedback">Please fill out this field.</div>
            </div>

            <div class="form-group">
                <label for="quantity">Quantity</label>
                <input type="number" class="form-control required" id="quantity" placeholder="optional" v-model="form.quantity">
                <div class="invalid-feedback">Only figures allowed</div>
            </div>
            <div class="form-group">
                <label for="unit-price">Unit Price</label>
                <input type="number" class="form-control required" id="unit-price" placeholder="price per unit of product/service" required v-model="form.price">
                <div class="invalid-feedback">Please fill out this field with figures only</div>
            </div>
            <div class="form-group mb-2">
                <label for="category">Advert Category</label>
                <select class="form-control" id="category"  required v-model="form.category">
                    <option>Foods</option>
                    <option>Services</option>
                    <option>Video Games</option>
                    <option>Fashion</option>
                    <option>Phones and Accessories</option>
                </select>
                <div class="invalid-feedback">Please select one option to continue.</div>
            </div>

            <div class="form-group">
              <label>Advert Image 
                <input type="file" id="file" v-on:change="handleFileUpload"/>
              </label>
              
            </div>
            
            <div class="form-group">
                <label for="description">Advert Description</label>
                <textarea class="form-control" id="description" rows="5" placeholder="clearly describe the features of your product here" v-model="form.description"></textarea>
            </div>

            <button class="btn btn-lg btn-blue" type="submit">Post Advert</button>
        </form>
        <p v-if="error" class="mt-2"><strong>{{ error }}</strong></p>
      </div>
        
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "adverts-create",
  data() {
    return {
      error: null,
     
      form: {
          name: null,
          price: null,
          quantity: null,
          description: null,
          file: null
      }
    };
  },

  methods: {
    
    handleFileUpload(event){
      this.form.file = event.target.files[0];
    },

    postAdvert() {
      let post_advert_url = `api/v1/${this.form.category}/adverts/create/`;

      let formData = new FormData();

      formData.append('name', this.form.name)
      formData.append('price', this.form.price)
      formData.append('quantity', this.form.quantity)
      formData.append('description', this.form.description)
      formData.append('file', this.form.file)
     
      let method = 'POST';
      
      apiService(post_advert_url, method, formData)
          .then(data => {
              this.$router.push({
                name: 'ad_detail', 
                params:{slug: data.slug}
              })
          })
          .catch(error => {this.error=error})
    }
  },

  mounted: function(){
    
    document.title = "Create Advert"
  }
}; 

</script>

<style scoped>

</style>
