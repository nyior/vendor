<template>
  <div class=" container advert mt-5 ">
    <div
      class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center"
    >
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

    <hr />
    <div v-if="UserHasReviewed">
      <p class="text-danger">You have reviewed this user in the past</p>
    </div>

    <div v-if="showForm">
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
            placeholder="required"
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
            placeholder="say something bro !!!"
            v-model="review_form.description"
          ></textarea>
        </div>

        <button class="btn btn-lg btn-blue" type="submit">Post Review</button>
      </form>
    </div>

    <div v-else>
      <div v-if="!UserHasReviewed">
        <button class="btn btn-blue" @click="showForm = true">
          review this user
        </button>
      </div>
    </div>

    <hr />

    <div
      class="row text-center d-flex justify-content-center align-items-center"
      v-for="(review, index) in reviews"
      :key="index"
      >
      <div class="col-12 col-md-6">
        <ReviewDetail
            :review="review"
            :requestUser="requestUser"
            @delete-review="deleteReview"
        />
      </div>
    </div>

    <div class="row text-center d-flex justify-content-center mt-4">
      <div class="col-6">
        <p v-show="loadingReviews">...loading...</p>
        <a v-show="next" @click="getReviews">
          <strong> Load More</strong>
        </a>
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";
import ReviewDetail from "@/components/ReviewDetail.vue";

export default {
  name: "user-detail",

  props: {
    id: {
      type: Number,
      required: true
    }
  },

  components: {
    ReviewDetail
  },

  data() {
    return {
      user: null,
      reviews: [],
      review_form: {
        duration: null,
        rating: null,
        description: null
      },

      error: null,
      UserHasReviewed: false,
      showForm: false,
      next: null,
      loadingReviews: false,
      requestUser: null
    };
  },

  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    getUser() {
      let get_user_url = `api/v1/users/${this.id}/`;

      apiService(get_user_url, "GET").then(data => {
        this.user = data;
        this.UserHasReviewed = data.current_user_has_reviewed;

        this.setPageTitle(data.username);
      });
    },

    getReviews() {
      let get_reviews_url = `api/v1/users/${this.id}/reviews/`;

      if (this.next) {
        get_reviews_url = this.next.slice(22);
      }

      this.loadingReviews = true;

      apiService(get_reviews_url, "GET").then(data => {
        this.reviews.push(...data.results);
        this.loadingReviews = false;
        if (data.next) {
          this.next = data.next;
        } else {
          this.next = null;
        }
      });
    },

    postReview() {
      let post_review_url = `api/v1/users/${this.user.id}/review-create/`;

      let formData = new FormData();

      formData.append("rating", this.review_form.rating);

      formData.append("description", this.review_form.description);

      let method = "POST";

      apiService(post_review_url, method, formData)
        .then(data => {
          this.reviews.unshift(data);
          this.showForm = false;
          this.UserHasReviewed = true;
        })
        .catch(error => {
          this.error = error;
        });
    },
    
    deleteReview(review) {
      let delete_review_url = `api/v1/reviews/${review.id}/`;

      apiService(delete_review_url, "DELETE").then(data => {
        this.$delete(this.reviews, this.reviews.indexOf(review));
        this.UserHasReviewed = false;
      });
    },

    setRequestUser(){
        this.requestUser = window.localStorage.getItem("username");
    }
  },

  mounted: function() {
    this.setRequestUser();
    this.getUser();
    this.getReviews();
  }
};
</script>

<style scoped></style>
