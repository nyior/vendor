<template>

  <nav class="navbar navbar-expand-lg py-3 shadow my-navbar  sticky-top">

    <router-link :to="{ name: 'home' }" class="navbar-brand pl-3">Marche`</router-link>

    <div class="collapse navbar-collapse">
      <form class="form-group has-search my-0 ml-auto mr-auto"
             @submit.prevent="onSubmit">
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

    <CategoryList />

  </nav>

</template>

<script>
  import CategoryList from "@/components/Category/CategoriesList.vue"

  export default {
    name: "NavbarComponent",

    components: {
      CategoryList
    },

    props: {
      authenticated: {
        type: Boolean,
        required: true
      }
    },

    data() {
      return {
        id: null,
        search_word: null
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
      },

      onSubmit(){
        this.$router.push({
              name: "search",
              params: { search_key: this.search_word }
        });
      },

      openNav(){
        document.getElementById("myNav").style.width = "70%";
      },
  
      closeNav(){
        document.getElementById("myNav").style.width = "0%";
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
    color: white !important;
    /* width: 100% */
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
