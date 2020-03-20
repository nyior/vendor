<template>
  <div class="home">
    <router-link class="sell" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>

    <div class="row m-0 w-100 h-100 home-hero">
      <div class="col-12 d-flex flex-column align-items-center px-5 justify-content-center text-center ml-3" style="position: relative">
        <div class="wrap-text">
          <h1 class="heading">Welcome to Marche</h1>
          <h4 class="mt-5">
            We help you discover products and services you are looking for on
            campus, and we help student entrepreneurs build successful businesses.
            We are Marche!
          </h4>
          <router-link :to="{ name: 'adverts' }">
            <button class="btn btn-lg mt-4 px-4">Explore</button>
          </router-link>
        </div>
        <!-- <img src="../assets/collage.png" alt=""> -->
      </div>
    </div>

    <h1 class="heading mt-4 mb-2 py-5">Discover Products and Services by Categories</h1>

    <div class="container">
      <div
        class="row m-0 w-100 categories p-2 px-md-5 py-3 mt-0 mb-2 text-center d-flex justify-content-center"
      >
        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Fashion' } }">
              <div class="mt-5">
                <img src="../assets/fashion.svg" class="categoryImage" alt="Responsive image" />
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>FASHION</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Electronic Appliances' } }">
              <div class="mt-5">
                <img src="../assets/monitor.svg" class="categoryImage" alt="Responsive image" />
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>ELECTRONIC APPLIANCES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Phones and Accessories' } }">
              <div class="mt-5">
                <img src="../assets/smartphone.svg" class="categoryImage" alt="Responsive image" />
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>PHONES AND ACCESSORIES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Video Games' } }">
              <div class="mt-5">
                <img src="../assets/console.svg" class="categoryImage" alt="Responsive image" />
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>VIDEO GAMES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Health and Beauty' } }">
              <div class="mt-5">
                <img src="../assets/medicine.svg" class="categoryImage" alt="Responsive image" />
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>HEALTH AND BEAUTY</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Services' } }">
              <div class="mt-5">
                <img src="../assets/select.svg" class="categoryImage" alt="Responsive image" />
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>SERVICES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Foods' } }">
              <div class="mt-5">
                <img src="../assets/fork.svg" class="categoryImage" alt="Responsive image" />
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>FOODS</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Others' } }">
              <div class="mt-5">
                <img src="../assets/others.svg" class="categoryImage" alt="Responsive image" />
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>OTHERS</strong>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "home",
  mounted: function() {
    document.title = "Marche`";
  }
};
</script>

<style scoped>
.home-hero {
  font-size: 1.4rem;
  background-image: linear-gradient(#7a09c4, #200135);
  color: white;
}

.btn {
  background-color: white !important;
  color: #200135 !important;
  font-weight: bold;
}

.fa:hover {
  color: #200135 !important;
}

.fa {
  font-size: 7rem !important;
  color: rgb(27, 21, 21) !important;
  font-weight: bold;
}

.categoryImage {
  height: 90px;
}

.col-md-3:nth-child(n + 5) {
  margin-top: 3rem;
}

.wrap-text {
  width: 50%;
}

.sell {
  position: fixed;
  bottom: 50px;
  right: 50px;
  z-index: 10;
}

.sell button{
  background: #f0f0f0!important;
  font-size: 1.5rem;
  padding: 1rem 1.2rem;
}

@media only screen and (max-width: 600px) {
  .categoryImage {
    height: 60px;
  }

  .col-md-3:nth-child(n + 5) {
    margin-top: 0rem;
  }

  .sell {
  position: fixed;
  bottom: 30px;
  right: 20px;
}
}
</style>
