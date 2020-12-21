<template>
  <nav class="navbar navbar-expand-lg py-3 shadow my-navbar  sticky-top">
    <i
      class="fa fa-long-arrow-left  pl-3"
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
      >Marche`</router-link
    >

    <div class="collapse navbar-collapse" v-if="!hide_nav_brand">
      <form
        class="form-group has-search my-0 ml-auto mr-auto"
        @submit.prevent="onSubmit"
      >
        <input
          class="form-control mr-sm-2 p-3 px-4"
          type="search"
          placeholder="Search and discover products/services on Marche"
          required
          v-model="search_word"
        />
      </form>

      <ul class="navbar-nav">
        <li class="nav-item mr-3">
          <router-link :to="{ name: 'adverts' }">
            <button class="btn  white-btn py-3">Explore</button>
          </router-link>
        </li>

        <li class="nav-item mr-3 mt-3" v-if="!is_authenticated">
          <a class="link" href="/accounts/login/">Login</a>
        </li>

        <li class="nav-item mt-3" v-if="!is_authenticated">
          <a class="link" href="/accounts/signup/">Register</a>
        </li>

        <li class="nav-item mr-3 mt-3" v-if="is_authenticated">
          <a class="link" href="/accounts/logout/">Logout</a>
        </li>

        <li class="nav-item mr-3 mt-3" v-if="is_authenticated">
          <router-link :to="{ name: 'wishlist' }">
            <a class="link">
              <i class="far fa-heart"></i>
            </a>
          </router-link>
        </li>

        <li class="nav-item mt-3" v-if="is_authenticated">
          <router-link :to="{ name: 'user_detail', params: { id: id } }">
            <a class="link">
              <i class="far fa-user"></i>
            </a>
          </router-link>
        </li>
      </ul>
    </div>

    <CategoryList v-if="!hide_nav_brand" />
  </nav>
</template>

<script>
import CategoryList from "@/components/Category/CategoriesList.vue";

import { user_id } from "@/common/global_variables.js";
import { is_authenticated } from "@/common/global_variables.js";

export default {
  name: "NavbarComponent",

  components: {
    CategoryList
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
      id: user_id,
      search_word: null,
      is_authenticated: is_authenticated
    };
  },

  methods: {
    onSubmit() {
      this.$router.push({
        name: "search",
        params: { search_key: this.search_word }
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

input[type="search"] {
  width: 50rem;
  height: 3rem;
  border-radius: 20px;
}

ul li {
  margin: 0rem 1.5rem;
}

#back-arrow {
  font-size: 2rem;
  color: white;
}
</style>
