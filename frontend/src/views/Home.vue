<template>
  <div class="home">
    <div class="row h-100 home-hero">
      <div
        class="col-12 col-md-6 mr-md-auto ml-md-auto d-flex flex-column justify-content-center  align-items-center  text-center ml-3"
      >
        <h1 class="heading">Welcome to Marche</h1>
        <h3 class="mt-2">
          We help you discover products and services you are looking for on
          campus, and we help student entrepreneurs build successful businesses.
          We are Marche!
        </h3>
        <router-link :to="{ name: 'adverts' }">
          <button class="btn btn-lg mt-2">Discover Available Products</button>
        </router-link>
      </div>
    </div>

    <h1 class="heading mt-4 mb-2">
      Discover Products and Services by Categories
    </h1>

    <div class="container">
      <div
        class="row  categories  p-5  mt-4 mb-2 text-center d-flex justify-content-center"
      >
        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Fashion' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>FASHION</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Electronic Appliances' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>ELECTRONIC APPLIANCES</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Phones and Accessories' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>PHONES AND ACCESSORIES</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Video Games' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>VIDEO GAMES</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Health and Beauty' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>HEALTH AND BEAUTY</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6  p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Services' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>SERVICES</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Foods' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
                <strong>FOODS</strong>
                
              </div>
            </router-link> 
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="card m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Others' } }"
            >
              <div class="mt-5">
                <i class="fa fa-shirtsinbulk"></i>
              </div>
              <hr />
              <div class="card-body text-muted">
                
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
</style>
