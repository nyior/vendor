<template>
  <div class=" container advert mt-5 ">
    <div class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center">
      
      <div class="col-md-4 col-6 p-0">
          
        <div class=" m-1 bg-grey mt-5">
            <a :href="user.profile_pic">
              <img
                :src="user.profile_pic"
                style="height: 18rem;"
                class="img-fluid m-1"
                alt="Responsive image"
              />
            </a>
            <div class="text-muted mt-2">
              <p>
                <a href="#">
                  <strong>
                    {{ user.username }} <br />
                    {{ user.phone_number }}<br />
                    {{ user.residence_hall }}
                  </strong>
                </a>
              </p>
            </div>
        </div>
      </div>
    </div>

    <hr>
        <div v-if="UserHasReviewed">
            <p class="text-danger">You have reviewed this user in the past</p>
        </div>
        

        <div v-if="showForm">
            <form 
                @submit.prevent="postReview" class="p-3 was-validated"  enctype="multipart/form-data">

            
                <div class="form-group">
                    <label for="quantity">Rating</label>
                    <input type="number" class="form-control required" id="quantity" placeholder="required" v-model="review_form.rating" required >
                    <div class="invalid-feedback">Only figures allowed</div>
                </div>
                
                <div class="form-group">
                    <label for="description">Advert Description</label>
                    <textarea class="form-control" id="description" rows="5" placeholder="say something bro !!!" v-model="review_form.description"></textarea>
                </div>

                <button class="btn btn-lg btn-blue" type="submit">Post Review</button>
            </form>
        </div>
        
        <div v-else>
            <div v-if="!UserHasReviewed">
                <button class="btn btn-blue" @click="showForm = true">review this user</button>
            </div>
        </div>
        

    <hr>

    <div class="row text-center d-flex justify-content-center align-items-center" v-for="review in reviews"
                     :key="review.id">
        <div class="col-12 col-md-6">
            <p>
                Rating: {{
                review.rating }} </p>

            <p>
                {{ review.description }}
            </p>
        </div>
    </div>
  </div>
</template>

<script>

import {apiService } from "../common/api.service.js";

export default {
  name: "user-detail",

  props: {
      id: {
          type: Number,
          required: true
      }
  },
  data() {
    return {
      user: null,
      reviews: [],
      review_form: {
          rating: null,
          description: null,
      },

      error: null,
      UserHasReviewed: false,
      showForm: false,
    };
  },

  methods: {

    setPageTitle(title){
        document.title = title;
    },

    getUser() {
     let get_user_url = `api/v1/users/${this.id}/`;

     apiService(get_user_url, 'GET')
          .then(data => {
              this.user=data
              this.UserHasReviewed = data.current_user_has_reviewed

              this.setPageTitle(data.username)
          })
    },

    getReviews(){
        let get_reviews_url = `api/v1/users/${this.id}/reviews/`;

        apiService(get_reviews_url, 'GET')
          .then(data => {
              this.reviews=data.results;
            
          })
    },

    postReview() {
        
      let post_review_url = `api/v1/users/${this.user.id}/review-create/`;

      let formData = new FormData();

      formData.append('rating', this.review_form.rating)

      formData.append('description', this.review_form.description)
     
      let method = 'POST';
      
      apiService(post_review_url, method, formData)
          .then(data => {
              this.reviews.unshift(data)
              this.showForm = false
          })
          .catch(error => {this.error=error})
    }

  },

  mounted: function() {
    this.getUser();
    this.getReviews();
  }
};
</script>

<style scoped>

</style>
