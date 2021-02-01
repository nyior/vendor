<template>
  <nav
    class="navbar navbar-expand-lg py-3 shadow my-navbar  sticky-top"
    id="my-nav"
  >
    <i
      class="fa fa-long-arrow-left"
      id="back-arrow"
      aria-hidden="true"
      @click="back"
      v-if="hide_nav_brand"
    ></i>

    <i class="navbar-brand  pl-md-5" v-if="hide_nav_brand">
      {{ title }}
    </i>

    <router-link
      :to="{ name: 'home' }"
      class="navbar-brand pacifico pl-3"
      v-if="!hide_nav_brand"
    >
     Vendor
    </router-link>

    <div class="collapse navbar-collapse" v-if="!hide_nav_brand">

      <SearchForm />

      <ul class="navbar-nav">
        <li class="nav-item mr-3">
          <router-link :to="{ name: 'adverts' }">
            <button class="btn  white-btn py-3">Explore</button>
          </router-link>
        </li>

        <li class="nav-item mr-3 mt-3" v-if="!isAuthenticated">
          <router-link :to="{ name: 'login' }">
            Login
          </router-link>
        </li>

        <li class="nav-item mt-3" v-if="!isAuthenticated">
          <router-link :to="{ name: 'register' }">
            Register
          </router-link>
        </li>

        <li class="nav-item mr-3" v-if="isAuthenticated">
          <button class="btn logout-btn py-3" @click="logout">
            Logout
          </button>
        </li>

        <li class="nav-item mr-3 mt-3" v-if="isAuthenticated">
          <router-link :to="{ name: 'wishlist' }">
            <a class="link">
              <i class="far fa-heart"></i>
            </a>
          </router-link>
        </li>

        <li class="nav-item mt-3" v-if="isAuthenticated">
          <router-link :to="{ name: 'user_detail', params: { id: userId } }">
            <a class="link">
              <i class="far fa-user"></i>
            </a>
          </router-link>
        </li>
      </ul>
    </div>

    <CategoryList :isAuthenticated="isAuth" v-if="!hide_nav_brand" />
  </nav>
</template>

<script>
import CategoryList from "@/components/Category/CategoriesList.vue";
import SearchForm from "@/components/Search/SearchForm.vue";

export default {
  name: "NavbarComponent",

  components: {
    CategoryList,
    SearchForm
  },

  props: {
    hide_nav_brand: {
      type: Boolean,
      required: true
    },

    title: {
      type: String,
      required: false
    }
  },

  data() {
    return {
      searchWord: null,
      isAuth: null
    };
  },

  computed: {
    isAuthenticated() {
      let isAuth = this.$store.state.isAuthenticated;
      if (isAuth === true) {
        this.isAuth = true;
        return true;
      } else {
        this.isAuth = false;
        return false;
      }
    },

    userId() {
      return this.$store.state.userId;
    }
  },

  methods: {
    onSubmit() {
      this.$router.push({
        name: "search",
        params: { search_key: this.searchWord }
      });
    },

    logout() {
      this.$store.dispatch("logoutAction");

      this.$router.push({
        name: "home"
      });
    },

    openNav() {
      document.getElementById("myNav").style.width = "70%";
    },

    closeNav() {
      document.getElementById("myNav").style.width = "0%";
    },

    back() {
      this.$router.back();
    }
  }
};
</script>

<style scoped>
a {
  color: white !important;
  font-weight: bold;
}

.my-navbar {
  font-size: 1.4rem;
  background-color: #7a09c4;
  color: white !important;
  /* width: 100% */
}

.navbar-brand {
  font-weight: bold;
  font-size: 2rem;
  color: white !important;
}

ul li {
  margin: 0rem 1.5rem;
}

#back-arrow {
  font-size: 2rem;
  color: white;
}

/* #my-nav .router-link-exact-active {
  color: #7a09c4 !important;
  cursor: pointer;
} */
</style>
