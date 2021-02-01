<template>
    <div class="container hide-on-mobile">
      <div class="row">
        <div class="col-12 col-md-10 ml-md-auto mr-md-auto text-center mt-5">
          <h1 class="heading mt-4 mb-2 py-5 px-md-5 px-3">
            Discover Products and Services by Categories
          </h1>
        </div>
      </div>

      <div
        class="row m-0 categories p-2 px-md-5 py-3 mt-0 mb-2 text-center d-flex justify-content-center"
      >
        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Fashion' } }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-female text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>FASHION</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{
                name: 'category',
                params: { category: 'Electronic Appliances' }
              }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-television text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>ELECTRONIC APPLIANCES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{
                name: 'category',
                params: { category: 'Phones and Accessories' }
              }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-mobile text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>GADGETS</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Video Games' } }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-gamepad text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>
              <div class="card-body pt-5 text-muted">
                <strong>VIDEO GAMES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{
                name: 'category',
                params: { category: 'Health and Beauty' }
              }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-medkit text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>HEALTH AND BEAUTY</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Services' } }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-handshake-o text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>SERVICES</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Foods' } }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-cutlery text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>FOODS</strong>
              </div>
            </router-link>
          </div>
        </div>

        <div class="col-md-3 col-6 p-0">
          <div class="m-2">
            <router-link
              :to="{ name: 'category', params: { category: 'Others' } }"
            >
              <div class="mt-5">
                <i
                  class="fa fa-question-circle text-muted categoryImage"
                  aria-hidden="true"
                ></i>
              </div>

              <div class="card-body pt-5 text-muted">
                <strong>OTHERS</strong>
              </div>
            </router-link>
          </div>
        </div>
      </div>
    </div>
</template>

<script>

export default {
  name: "categories",

};
</script>

<style scoped>

.fa:hover {
  color: #200135 !important;
}

.fa {
  font-size: 7rem !important;
  color: rgb(27, 21, 21) !important;
  font-weight: bold;
}

.col-md-3:nth-child(n + 5) {
  margin-top: 3rem;
}

@media only screen and (max-width: 600px) {
  
  .col-md-3:nth-child(n + 5) {
    margin-top: 0rem;
  }
}
</style>
