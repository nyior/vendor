<template>
  <div class=" container products">
    <div
      class="row  categories  p-5 mt-5  mb-2 text-left d-flex justify-content-center align-items-center"
    >
      <div class="col-md-6 col-12 mt-5 shadow border">
        <h1 class="heading mt-4 mb-2">
          Edit Your Review
        </h1>

        <form
        @submit.prevent="postReview"
        class="p-3 was-validated"
        enctype="multipart/form-data"
      >
        <div class="form-group">
          <label for="quantity">Rating</label>
          <input
            type="number"
            class="form-control required"
            id="quantity"
            
            v-model="review_form.rating"
            required
          />
          <div class="invalid-feedback">Only figures allowed</div>
        </div>

        <div class="form-group">
          <label for="description">Advert Description</label>
          <textarea
            class="form-control"
            id="description"
            rows="5"
            
            v-model="review_form.description"
          ></textarea>
        </div>

        <button class="btn btn-lg btn-blue" type="submit">Post Review</button>
      </form>
        <p v-if="error" class="mt-2">
          <strong>{{ error }}</strong>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "review-update",

  props: {
      id: {
          type: Number,
          required: true,
      },

      reviewee_id: {
          type: Number,
          required: true,
      },

      rating: {
          type: Number,
          required: true,
      },
      description: {
          type: String,
          required: true,
      }
  },
  data() {
    return {
      error: null,

      review_form: {
        rating: this.rating,
        description: this.description
      },

    };
  },

  async beforeRouteEnter(to, from, next){
      let get_review_url = `api/v1/reviews/${to.params.id}/`;
      

      let data = await apiService(get_review_url, "GET");
      to.params.rating = data.rating;
      to.params.description = data.description;
      to.params.reviewee_id = data.reviewee;

      return next();
  },


  methods: {
    postReview() {
      let post_review_url = `api/v1/reviews/${this.id}/`;

      let method = "PUT";

      apiService(post_review_url, method, this.review_form)
        .then(() => {
          this.$router.push(
              {
                  name: 'user_detail',
                  params: { id: this.reviewee_id }
              }
          )
        })
        .catch(error => {
          this.error = error;
        });
    }
  },

  mounted: function() {
    document.title = "Update Review";
  }
};
</script>

<style scoped></style>
