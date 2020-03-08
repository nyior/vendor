<template>
  
      <div class=" p-0 mt-5">
        
        <div>duration : {{ review.duration }} ago</div>
        
        <div class="text-muted mt-2">
          <p>
            <strong>
              {{ review.description }}
            </strong>
          </p>

          <hr />
          <p>rating: {{ review.rating }}</p>
        </div>

        <div class="" v-if="isReviewAuthor">
            <button class="btn btn-blue mr-2">Edit Review</button>
            <button @click="DeleteReviewTrigger" class="btn btn-blue ml-2" >Delete Review</button>
        </div>
      </div>
    
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "review-detail",

  props: {
    review: {
      type: Object,
      required: true
    },

    requestUser: {
      type: String,
      required: true
    }
  },

  data() {
    return {
      
    };
  },
  
  computed: {
      isReviewAuthor(){
          return this.review.reviewer === this.requestUser;
      }
  },

  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    DeleteReviewTrigger(){
      this.$emit('delete-review', this.review);
    }
  },

  mounted: function() {
  
    this.setRequestUser();
  }
};
</script>

<style scoped></style>
