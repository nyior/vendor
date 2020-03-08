<template>
  <div class=" container advert mt-5 ">
    <div
      class="row    mt-5 mb-2 text-center d-flex justify-content-center align-items-center"
    >
      <div class="col-md-6 col-12 p-0 mt-5">
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
      </div>
    </div>
  </div>
</template>

<script>
import { apiService } from "../common/api.service.js";

export default {
  name: "review-detail",

  props: {
    id: {
      type: Number,
      required: true
    }
  },
  data() {
    return {
      review: null
    };
  },

  methods: {
    setPageTitle(title) {
      document.title = title;
    },

    getReview() {
      let get_review_url = `api/v1/reviews/${this.id}/`;

      apiService(get_review_url, "GET").then(data => {
        this.review = data;
        this.setPageTitle(data.description);
      });
    }
  },

  mounted: function() {
    this.getReview();
  }
};
</script>

<style scoped></style>
