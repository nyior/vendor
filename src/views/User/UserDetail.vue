<template>
  <div class="container-fluid mt-0">
    
    <div v-if="loadingUser" class="row pt-5 mt-5">
        <div class="col-12 text-center ">
            <h3> ...loading user...</h3>
        </div>
    </div>  
    
    <div v-else class="row px-md-5 px-3 dp-image-cover">
      <div class="col-12 text-center ">
        <div class="card">
          <div class="mt-5">
            <div>
              
              <div class="profilePicContainer mt-5">
                <a :href="user.profile_picture">
                    <img
                        :src="user.profile_picture"
                        class="img-fluid"
                    />
                </a>
        
                <i 
                    v-if="UserHasProfile && !showAvatarUpdateForm"
                    id="update-profile-avatar"
                    class="fa fa-edit" 
                    aria-hidden="true"
                    @click="showAvatarUpdateForm = true"
                >
                </i>
              </div>
              

              <div v-if="showAvatarUpdateForm">
                <form
                  @submit.prevent="UpdateAvatar"
                  class="p-3"
                  enctype="multipart/form-data"
                >
                  <div class="form-group">
                    <label>
                      <input
                        type="file"
                        ref="file"
                        v-on:change="handleFileUpload"
                      />
                    </label>
                  </div>

                  <LoaderButton 
                    :status="updatingAvatar" 
                    :text="avatarText"
                  />
                  
                  <div class="mt-2">
                    <i 
                        class="fa fa-times" 
                        aria-hidden="true"
                        @click="showAvatarUpdateForm = false">
                            close
                    </i>
                  </div>
                </form>
              </div>
            </div>

            <div class="mt-5" v-if="!showProfileUpdateForm">
                <p id="username">{{ user.username }}</p>      
            </div>

            <div class="my-5 py-5" v-if="!showProfileUpdateForm">
                <div>
                    <span>mobile number : {{ user.phone_number }}</span>
                </div>
                <div>
                    <span>residence hall : {{ user.residence_hall }}</span>
                </div>
            </div>

            <div v-if="showProfileUpdateForm">
              <UpdateUserProfileForm
                :user="user"
                :status="updatingUserProfile"
                @update-profile="UpdateProfile"
                @hide-form="showProfileUpdateForm = false"
              />
            </div>

            <div v-if="UserHasProfile && !showProfileUpdateForm">
              <button
                class="blue-btn btn-block"
                @click="showProfileUpdateForm = true"
              >
                <i 
                    class="fa fa-edit" 
                    id="edit-profile"
                    aria-hidden="true"
                >
                </i>
                edit profile
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <div class="row   px-md-5 px-3 py-5 my-5">
      <div class="col-12 text-center">
        <h1 class="heading" v-if="UserHasProfile">
          <strong>Your Shop</strong>
        </h1>
        <h1 class="heading" v-else><strong>Seller's Shop</strong></h1>
      </div>

      <div class="row px-md-5 px-3 py-5 my-5" v-if="!sellerHasItems">
          <div class=" col-12 text-center">
            <h2 class="text-danger px-3">
            Your shop is empty. Sell on Marche to populate your shop
            </h2>
            <router-link 
            :to="{ name: 'ads_create' }"
            class="blue-btn btn block mt-2"
                            
            >
                upload items
            </router-link>
        </div>
      </div>

      <div  v-else class="row  text-center">
        <div
          class="col-md-3 col-12 px-5"
          v-for="advert in sellerShop"
          :key="advert.id"
        >
          <AdvertMinified :advert_object="advert" />
        </div>
      </div>
    </div>

    <div class="row text-center d-flex justify-content-center mt-4">
      <div class="col-6">
        <a v-show="more" @click="getUserAdverts">
          <strong>Load More</strong>
        </a>
      </div>
    </div>

    <!-- <hr />

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
    </div> -->

    <!-- <div v-else>
      <div v-if="!UserHasProfile">
        <button class="blue-btn btn-block" @click="showForm = true">
          review this user
        </button>
      </div>
    </div> -->

    <!-- <hr />

    <div
      class="row text-center d-flex justify-content-center align-items-center"
    >
      <div
        class="col-12 col-md-6"
        v-for="(review, index) in reviews"
        :key="index"
      >
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
          <strong>Load More</strong>
        </a>
      </div>
    </div> -->
  </div>
</template>

<script>
import { apiService } from "@/common/api.service.js";

import ReviewDetail from "@/components/Reviews/ReviewDetail.vue";
import UpdateUserProfileForm from "@/components/User/UpdateUserProfileForm.vue";
import AdvertMinified from "@/components/Adverts/AdvertMinified.vue";
import LoaderButton from "@/components/Utils/LoaderButton.vue";

import { store } from "@/store/store";

export default {
  name: "adverts-category",

  components: {
    ReviewDetail,
    UpdateUserProfileForm,
    AdvertMinified,
    LoaderButton
  },

  props: {
    id: {
      type: Number,
      required: false
    }
  },

  data() {
    return {
      sellerShop: [],
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
      more: null,
      loadingReviews: false,
      loadingUser: false,
      loadingAdverts: false,
      updatingAvatar: false,
      updatingUserProfile: false,
      requestUser: null
    };
  },

  computed: {
    UserHasProfile() {
      return this.requestUser === this.user.username;
    },

    isAuthenticated() {
      return store.state.isAuthenticated;
    },

    sellerHasItems(){
        return this.sellerShop.length > 0;
    },

    avatarText() {
        return "upload avatar";
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
      this.loadingUser = true;
      let get_user_url = `api/v1/users/${this.id}/`;

      apiService(get_user_url, "GET").then(data => {
        
        this.user = data;
        this.loadingUser = false;
        this.UserHasReviewed = data.current_user_has_reviewed;

        this.setPageTitle(data.username);
      })
      .catch(error => {
          this.loadingUser = false;
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

    getUserAdverts() {
      let get_shop_url = `api/v1/user/${this.id}/shop/`;

      if (this.more) {
        get_shop_url = this.more.slice(22);
      }

      this.loadingAdverts = true;

      apiService(get_shop_url, "GET").then(data => {
        this.sellerShop.push(...data.results);
        this.loadingAdverts = false;

        if (data.next) {
          this.more = data.next;
        } else {
          this.more = null;
        }
      })
      .catch(error => {
          this.loadingAdverts = false;
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
      this.updatingUserProfile = true;
      let updateprofile_url = `api/v1/users/${formData.user_id}/`;

      let method = "PUT";

      apiService(updateprofile_url, method, formData)
        .then(data => {
          this.user = data;
          this.updatingUserProfile = false;
          this.requestUser = data.username;
          this.showProfileUpdateForm = false;
        })
        .catch(error => {
          this.updatingUserProfile = false;
          this.error = error;
        });
    },

    UpdateAvatar() {
      this.updatingAvatar = true;
      let updateprofile_url = `api/v1/avatar/`;

      let formData = new FormData();

      formData.append("profile_picture", this.avatar);
      let method = "PUT";

      apiService(updateprofile_url, method, formData)
        .then(data => {
          this.user.profile_picture = data.profile_picture;
          this.showAvatarUpdateForm = false;
          this.updatingAvatar = false;
        })
        .catch(error => {
          this.updatingAvatar = false;
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

    setRequestUser() {
      this.requestUser = this.$store.state.username;
    }
  },

  mounted: function() {
    this.setRequestUser();
    this.getUser();
    // this.getReviews();
    this.getUserAdverts();
  },

  async beforeRouteEnter(to, from, next) {
    let isAuth = store.state.isAuthenticated;
    if (isAuth === true) {
      next();
    } else {
      next({
        name: "continue" // back to safety route //
      });
    }
  }
};
</script>

<style scoped>
.profilePicContainer {
  width: 150px;
  height: 150px;
  display: flex;
  justify-content: center;
  margin: auto;
  border-radius: 50%;
  border-style: solid;
  border-color: #FFFFFF;
  box-shadow: 0 0 8px 3px #B8B8B8; 
  position: relative;
}

.profilePicContainer img {
  height: 100%;
  width: 100%;
  border-radius: 50%;
}


#update-profile-avatar{
  position: absolute;
  bottom: 10%;
  right: 0%;
  border-radius: 50%;
  height: 30px;
  width: 30px;
  display: flex !important;
  align-items: center;
  justify-content: center;
  background-color: white;
  color: cornflowerblue;
  box-shadow: 0 0 8px 3px #B8B8B8;
}

#username {
  color:white;
  font-size: 3rem;
  font-weight: bold;
  letter-spacing: 0.1rem;
}

a:hover {
  color: black !important;
}

span{
    color: red !important;
    margin-top: 0.2rem;
    font-size: 1.2rem;
}

.card{
 background-color: #C0C0C0;
}

span{
    font-size: 1.6rem;
    letter-spacing: 0.1rem;
    color: white;
    font-weight: bold;
}
</style>
