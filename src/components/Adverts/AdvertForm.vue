<template>
    <div
      class="row p-5 mt-5  mb-2 text-left d-flex  justify-content-center align-items-center"
    >
      <div class="col-md-6 col-12 mt-5 shadow border px-3 py-3">
        <form
          @submit.prevent="onSubmit"
          class="p-3 was-validated"
          enctype="multipart/form-data"
        >
          <div class="form-group mb-5 mt-3 text-center">
            <label for="file" style="cursor: pointer;">
              <img
                :src="img_src"
                class="img-fluid"
                id="product-image"
                width="600"
                height="300"
              />
              <p>tap to add an image</p>
            </label>

            <input
              type="file"
              required
              ref="file"
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
              <option>Electronic Appliances</option>
              <option>Health and Beauty</option>
              <option>Others</option>
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

          <LoaderButton 
                :status="isLoading" 
                :text="text"
          />
        </form>

        <p v-if="error" class="mt-2 text-danger">
          <strong>{{ error }}</strong>
        </p>
      </div>
    </div>
</template>

<script>
import LoaderButton from "@/components/Utils/LoaderButton.vue";

export default {
  name: "advert-form",

  components: {
    LoaderButton
  },

  props: {
    responseData: {
      type: Object,
      required: false
    }
  },

  data() {
    return {
      error: null,
      isLoading: false,

      img_src: null,

      text: "create",

      form: {
        name: this.responseData.name,
        price: this.responseData.price,
        quantity: this.responseData.quantity,
        description: this.responseData.description,
        file: this.responseData.file,
        category: this.responseData.category
      },

      has_file: this.file == null ? false : true
    };
  },

  methods: {
    handleFileUpload(event) {
      this.form.file = event.target.files[0];
      this.img_src = URL.createObjectURL(event.target.files[0]);
    },

    onSubmit(){
        this.$emit("create-ad", this.form)
    }
  }
};
</script>

<style scoped>
</style>
