<template>

  <div class=" container products">

    <div class="row  categories  p-5 mt-5  mb-2 text-left d-flex  justify-content-center align-items-center">
      <div class="col-12 text-center ">
        <h1 class="heading mt-5 mb-2">
            Create an Advert 
        </h1>
      </div>

      <div class="col-md-6 col-12 mt-5 shadow border px-3 py-3">

        <form
          @submit.prevent="postAdvert"
          class="p-3 was-validated"
          enctype="multipart/form-data"
        >

          <div class="form-group mb-5 mt-3 text-center">
          
            <label for="file" style="cursor: pointer;">
            
              <img :src="img_src"  class="img-fluid rounded"  
                  id="product-image"
                  width="300" 
                  height="200"
              />

            </label>

            <input type="file" 
                required ref="file"  
                v-on:change="handleFileUpload" 
                accept="image/gif, image/jpeg, image/png" 
                style="display: none;" 
                id="file"
            /> 

                    
          </div>
          
          <div class="form-group mt-3">
            <label for="advert-name">Advert Name</label>
            <input
              type="text"
              class="form-control"
              id="advert-name"
              placeholder="example: Iphone 5 64GB Gold"
              required
              v-model="form.name"
            />
            <div class="invalid-feedback">Please fill out this field.</div>
          </div>

          <div class="form-group mt-3">
            <label for="quantity">Quantity</label>
            <input
              type="number"
              min="0"
              class="form-control required"
              id="quantity"
              placeholder="optional"
              v-model="form.quantity"
            />
            <div class="invalid-feedback">Only figures allowed</div>
          </div>

          <div class="form-group mt-3">
            <label for="unit-price">Unit Price</label>
            <input
              type="number"
              min="0"
              class="form-control required"
              id="unit-price"
              placeholder="price per unit of product/service"
              required
              v-model="form.price"
            />
            <div class="invalid-feedback">
              Please fill out this field with figures only
            </div>
          </div>

          <div class="form-group mb-2 mt-3">
            <label for="category">Advert Category</label>
            <select
              class="form-control"
              id="category"
              required
              v-model="form.category"
            >
              <option>Foods</option>
              <option>Services</option>
              <option>Video Games</option>
              <option>Fashion</option>
              <option>Phones and Accessories</option>
            </select>
            <div class="invalid-feedback">
              Please select one option to continue.
            </div>
          </div>

          <div class="form-group mt-3">
            <label for="description">Advert Description</label>
            <textarea
              class="form-control"
              id="description"
              rows="5"
              placeholder="clearly describe the features of your product here"
              v-model="form.description"
            ></textarea>
          </div>

          <button class="btn  blue-btn" type="submit">create</button>
        </form>

        <p v-if="error" class="mt-2">
          <strong>{{ error }}</strong>
        </p>

      </div>

    </div>

    <!-- <div class="row  p-5  d-flex  justify-content-center align-items-center"
          >

      <div class="col-md-6 col-12 mt-5 px-3 py-3">

         <router-view ></router-view>

      </div>
    </div> -->

  </div>

</template>

<script>

  import { apiService } from "@/common/api.service.js";
  import { is_authenticated } from "@/common/global_variables.js";

  import JoinMarche from "@/components/Modals/JoinMarche.vue";

  export default {
    name: "adverts-create",

    components: {
      JoinMarche
    },

    props: {
      slug: {
        type: String,
        required: false,
      },

      category: {
        type: String,
        required: false,
      },

      name: {
            type: String,
            required: false,
      },

      price: {
            type: Number,
            required: false,
      },

      quantity: {
            type: Number,
            required: false,
      },

    
      description: {
            type: String,
            required: false,
        },

      file: {
            type: String,
            required: false,
        }
    },

    data() {
      return {
        error: null,

        img_src: null,

        form: {
          name: this.name,
          price: this.price,
          quantity: this.quantity,
          description: this.description,
          file: this.file,
          category: this.category
        }, 

        is_authenticated: is_authenticated
      };
    },

    methods: {
      handleFileUpload(event) {
        this.form.file = event.target.files[0];
        this.img_src = URL.createObjectURL(event.target.files[0]);
      },

      postAdvert() {
        let post_advert_url = `api/v1/adverts/`;

        let method = "POST";
        let file = this.form.file;
        let formData = new FormData();
        
        if (this.slug !== undefined) {
          //this.$refs.file.value = this.file;
          post_advert_url = `api/v1/adverts/${this.slug}/`;
          method = 'PUT';
        }
        
        formData.append("category", this.form.category);
        formData.append("name", this.form.name);
        formData.append("price", this.form.price);
        formData.append("quantity", this.form.quantity);
        formData.append("description", this.form.description);
        formData.append("file", file);

        apiService(post_advert_url, method, formData)
          .then(data => {
            this.$router.push({
              name: "ad_detail",
              params: { slug: data.slug }
            });
          })
          .catch(error => {
            this.error = error;
          });
      }
    },

    async beforeRouteEnter(to, from, next){

      if (to.params.slug !== undefined && is_authenticated) {
        let get_advert_url = `api/v1/adverts/${to.params.slug}/`;
        
        let data = await apiService(get_advert_url, "GET");
        to.params.name = data.name;
        to.params.price = data.price;
        to.params.quantity = data.quantity;
        to.params.description = data.description;
        to.params.file = data.file;
        to.params.category = data.category;

        return next();
      } else if(!is_authenticated) {

        return next({
          name: 'continue' // back to safety route //
        });

      } else {

        return next();
        
      }
      
    },

    mounted: function() {
      //this.setFileField();
      document.title = "Create Advert";

    }
  };
  
</script>

<style scoped>

  #product-image{
      background-color: grey;
  }

  p{
    z-index: 1;
  }

</style>
