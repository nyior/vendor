<template>
  <div class=" container advert mt-5 ">
    <div
      class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center"
    >
      <div class="col-md-4 col-6 p-0">
        <div class=" m-1 bg-grey mt-5">
          <div>
            <a :href="user.profile_picture">
            <img
              :src="user.profile_picture"
              style="height: 18rem;"
              class="img-fluid m-1"
              alt="Responsive image"
            />
            </a>

            <div v-if="UserHasProfile && !showAvatarUpdateForm">
              <button class="btn btn-blue" @click="showAvatarUpdateForm = true">
                change display picture
              </button>
            </div>

            <div v-if="showAvatarUpdateForm ">
              <form
                @submit.prevent="UpdateAvatar"
                class="p-3 "
                enctype="multipart/form-data"
              >
                <div class="form-group">
                  <label
                    >
                    <input type="file" ref="file"  v-on:change="handleFileUpload" />
                  </label>
                </div>

                <button class="btn btn-lg btn-blue" type="submit">Post Avatar</button>
              </form>
            </div>
          </div>
          
          <div class="text-muted mt-2" v-if="!showProfileUpdateForm">
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
          <div v-if="showProfileUpdateForm">
            <UpdateUserProfileForm
                :user="user"
                @update-profile="UpdateProfile"
            />
          </div>

          <div v-if="UserHasProfile && !showProfileUpdateForm">
            <button class="btn btn-blue" @click="showProfileUpdateForm = true">
              edit profile
            </button>
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
          <label for="description">Say something about this user</label>
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
import UpdateUserProfileForm from "@/components/UpdateUserProfileForm.vue";

export default {
  name: "user-detail",

  props: {
    id: {
      type: Number,
      required: true
    }
  },

  components: {
    ReviewDetail,
    UpdateUserProfileForm
  },

  data() {
    return {
      user: null,
      avatar: null,
      reviews: [],
      review_form: {
        duration: null,
        rating: null,
        description: null
      },

      error: null,
      UserHasReviewed: false,
      showForm: false,
      showProfileUpdateForm: false,
      showAvatarUpdateForm: false,
      next: null,
      loadingReviews: false,
      requestUser: null
    };
  },

  computed: {
    UserHasProfile(){
      return this.requestUser == this.user.username;
    }
  },

  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    handleFileUpload(event) {
      this.avatar = event.target.files[0];
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

    UpdateProfile(formData) {
      let updateprofile_url = `api/v1/users/${formData.user_id}/`;

      let method = "PUT";

      apiService(updateprofile_url, method, formData)
        .then(data => {
          this.user  = data;
          this.requestUser = data.username;
          this.showProfileUpdateForm = false;
        })
        .catch(error => {
          this.error = error;
        });
    },

    UpdateAvatar() {
      let updateprofile_url = `api/v1/avatar/`;

      let formData = new FormData();

      formData.append("profile_picture", this.avatar);
      let method = "PUT";

      apiService(updateprofile_url, method, formData)
        .then(data => {
          this.user.profile_picture  = data.profile_picture;  
          this.showAvatarUpdateForm = false; 
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
  },
};
</script>

<style scoped></style>
