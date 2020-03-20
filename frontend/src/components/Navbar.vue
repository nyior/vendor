<template>
  <nav class="navbar navbar-expand-lg py-3 shadow my-navbar fixed-top">
    <router-link :to="{ name: 'home' }" class="navbar-brand pl-3">Marche`</router-link>

    <div class="collapse navbar-collapse" id="navbarSupportedContent">
      <form class="form-group has-search my-0 ml-auto mr-auto">
        <input
          class="form-control mr-sm-2 p-3 px-4"
          type="search"
          placeholder="Search and discover products/services on Marche"
        />
      </form>

      <ul class="navbar-nav">
        <li class="nav-item mr-3">
          <router-link :to="{ name: 'adverts' }">
            <button class="btn btn-lg">Explore</button>
          </router-link>
        </li>

        <li class="nav-item mr-3 mt-2" v-if="!is_authenticated">
          <a class="link" href="/accounts/login/">Login</a>
        </li>
        <li class="nav-item mt-2" v-if="!is_authenticated">
          <a class="link" href="/accounts/signup/">Register</a>
        </li>

        <li class="nav-item mr-3 mt-2" v-if="is_authenticated">
          <a class="link" href="/accounts/logout/">Logout</a>
        </li>
        <li class="nav-item mt-2 mr-3" v-if="is_authenticated">
          <router-link :to="{ name: 'wishlist' }">
            <a class="link">
              <i class="far fa-heart"></i>
            </a>
          </router-link>
        </li>
        <li class="nav-item mt-2" v-if="is_authenticated">
          <router-link :to="{ name: 'user_detail', params: { id: id } }">
            <a class="link">
              <i class="far fa-user"></i>
            </a>
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  name: "NavbarComponent",

  props: {
    authenticated: {
      type: Boolean,
      required: true
    }
  },

  data() {
    return {
      id: null
    };
  },

  computed: {
    is_authenticated() {
      return this.authenticated;
    }
  },

  methods: {
    setUserId() {
      this.id = window.localStorage.getItem("user_id");
    }
  },

  mounted: function() {
    this.setUserId();
  }
};
</script>

<style scoped>
@import url("https://fonts.googleapis.com/css?family=Pacifico&display=swap");

.my-navbar {
  font-size: 1.4rem;
  background-color: #7a09c4;
  font-weight: bold;
  width: 100%
}
.btn {
  background-color: white !important;
  color: #200135 !important;
  font-weight: bold;
}

.navbar-brand {
  font-weight: bold;
  font-size: 2rem;
  font-family: "Pacifico";
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
</style>
