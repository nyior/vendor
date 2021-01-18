<template>
  <div>
    <div class="overlay " id="myNav" v-on:click="closeNav">
      <a href="javascript:void(0)" class="closebtn" v-on:click="closeNav"
        >&times;</a
      >

      <div class="overlay-header text-center px-5">
        <P>Categories</P>
      </div>
      <ul class="overlay-content px-5 navbar-nav text-center">
        <li class="nav-item ">
          <router-link :to="{ name: 'adverts' }">
            All
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{ name: 'category', params: { category: 'Fashion' } }"
          >
            Fashion
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{
              name: 'category',
              params: { category: 'Electronic Appliances' }
            }"
          >
            Electronic Appliances
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{
              name: 'category',
              params: { category: 'Phones and Accessories' }
            }"
          >
            Phones/Accessories
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{ name: 'category', params: { category: 'Video Games' } }"
          >
            Video Games
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{ name: 'category', params: { category: 'Services' } }"
          >
            Services
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{
              name: 'category',
              params: { category: 'Health and Beauty' }
            }"
          >
            Health and Beauty
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{ name: 'category', params: { category: 'Foods' } }"
          >
            Foods
          </router-link>
        </li>

        <li class="nav-item mt-4">
          <router-link
            :to="{ name: 'category', params: { category: 'Others' } }"
          >
            Others
          </router-link>
        </li>

        <li class="nav-item  mt-3" v-if="!isAuthenticated">
          <router-link :to="{ name: 'login' }">
            <button class="btn color-purple white-btn py-3">
                Join
            </button>
          </router-link>
        </li>
        <li class="nav-item  mt-3" v-else>
            <button class="btn color-purple white-btn py-3">
                Logout
            </button>
        </li>
      </ul>
    </div>

    <span class="mr-2 hide-elem" v-on:click="openNav">
      <i class="fa fa-bars" aria-hidden="true"></i>
    </span>
  </div>
</template>

<script>

export default {
  name: "categories-list",

  computed: {
    isAuthenticated(){
        return this.$store.state.isAuthenticated;
    }
  },

  methods: {
    openNav() {
      document.getElementById("myNav").style.width = "70%";
    },

    closeNav() {
      document.getElementById("myNav").style.width = "0%";
    }
  }
};
</script>

<style scoped>
i {
  color: white !important;
  font-size: 2rem;
}

a {
  text-decoration: none;
  color: white !important;
  font-size: 1.6rem;
}

a.color-purple {
  color: #7a09c4 !important;
  font-weight: bold;
}

.overlay {
  height: 100%;
  width: 0%;
  position: fixed; /* Stay in place */
  z-index: 1; /* Sit on top */
  right: 0;
  bottom: 0;
  top: 0;
  background-color: rgb(0, 0, 0); /* Black fallback color */

  background-color: #56078c;
  overflow-x: hidden !important; /* Disable horizontal scroll */
  overflow-y: hidden !important;
  transition: 0.5s; /* 0.5 second transition effect to slide in or slide down the overlay (height or width, depending on reveal) */
}

/* Position the content inside the overlay */
.overlay-content {
  position: relative;
  top: 20%; /* 25% from the top */
  width: 100%; /* 100% width */
  text-align: center; /* Centered text/links */
  margin-top: 10px; /* 30px top margin to avoid conflict with the close button on smaller screens */
}

.overlay-header {
  position: relative;
  top: 15%;
  width: 100%;
  margin-top: 10px;
  font-size: 2rem;
  font-weight: bold;
}

.overlay .closebtn {
  position: absolute;
  top: 10px;
  right: 15px;
  font-size: 4rem;
  font-weight: bold;
}

@media only screen and (max-width: 600px) {
  .overlay .closebtn {
    top: 15px;
    right: 35px;
  }
}

@media only screen and (min-width: 600px) {
  .hide-elem {
    display: None;
  }
}
</style>
