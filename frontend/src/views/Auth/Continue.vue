<template>
  <div>
    <div class="row continue-hero px-5">
      <div
        class="col-12 col-md-10 ml-md-auto mr-md-auto d-flex flex-column align-items-center text-center "
      >
        <div class="hero-text">
          <h4 class="mt-5 sub-heading">
            oops‼ This feature is only available to logged in users. To
            login/signup click the button below.
          </h4>
          <a class="link" href="/accounts/login/">
            <button class="btn mt-4 py-3 blue-btn">continue</button>
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const self = this;
export default {
  name: "JoinMarche",

  methods: {
    close() {
      this.$router.back();
    }
  }
};
</script>

<style scoped>
.continue-hero {
  padding-bottom: 15rem;
  overflow-y: hidden;
}

.hero-text {
  margin-top: 15rem;
}
</style>
