<template>
  <div class="home">
    <router-link class="sell hide-on-mobile" :to="{ name: 'ads_create' }">
      <button class="btn btn-lg">Sell on Marche</button>
    </router-link>

    <div class="row home-hero">
      <div class="col-12 col-md-10 ml-md-auto mr-md-auto d-flex flex-column align-items-center text-center ">
        <div class="hero-text">
          <h1 class="heading">Welcome to Marche</h1>
          <h4 class="mt-5 sub-heading">
            We help you discover products and services you are looking for on
            campus, and we help student entrepreneurs build successful businesses.
            We are Marche!
          </h4>
          <router-link :to="{ name: 'adverts' }">
            <button class="btn btn-lg mt-4 py-3 white-btn">Explore</button>
          </router-link>
        </div>
        <!-- <img src="../assets/collage.png" alt=""> -->
      </div>
    </div>

    <div class="col-12 col-md-10 ml-md-auto mr-md-auto text-center mt-5">
      <h1 class="heading mt-4 mb-2 py-5">
        Discover Products and Services by Categories
      </h1>
    </div>

    <div class="container">
      <div
        class="row m-0 categories p-2 px-md-5 py-3 mt-0 mb-2 text-center d-flex justify-content-center"
      >
        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Fashion' } }">
              <div class="mt-5">
          
                <i class="fa fa-female text-muted categoryImage" aria-hidden="true"></i>
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

                <i class="fa fa-television text-muted categoryImage" aria-hidden="true"></i>
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
               
                <i class="fa fa-mobile text-muted categoryImage" aria-hidden="true"></i>
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>GADGETS</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link :to="{ name: 'category', params: { category: 'Video Games' } }">
              <div class="mt-5">

                <i class="fa fa-gamepad text-muted categoryImage" aria-hidden="true"></i>

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
          

                <i class="fa fa-medkit text-muted categoryImage" aria-hidden="true"></i>
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
                <i class="fa fa-handshake-o text-muted categoryImage" aria-hidden="true"></i>
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

                <i class="fa fa-cutlery text-muted categoryImage" aria-hidden="true"></i>
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

                <i class="fa fa-question-circle text-muted categoryImage" aria-hidden="true"></i>
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
    background-image: linear-gradient(#7a09c4, #200135);
    color: white;
    height: 100%;
    background-position: center;
    background-repeat: no-repeat;
    background-size: cover;
  }

  .hero-text {
      margin-top:15rem;
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
    font-size: 20rem;
    color: black;
    opacity: 0.5;
  }

  .col-md-3:nth-child(n + 5) {
    margin-top: 3rem;
  }


  @media only screen and (max-width: 600px) {
    .categoryImage {
      height: 60px;
    }

    .col-md-3:nth-child(n + 5) {
      margin-top: 0rem;
    }

    .hero-text {
      margin-top:10rem;
  }
  }
</style>
