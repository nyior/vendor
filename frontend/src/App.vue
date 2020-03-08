<template>
  <div id="app">
    <NavbarComponent />
    <router-view />
  </div>
</template>

<script>
import NavbarComponent from "./components/Navbar.vue";
import { apiService } from "./common/api.service.js";

export default {
  name: "App",
  components: {
    NavbarComponent
  },

  methods: {
    async setUserInfo(){
      let get_user_url = `api/v1/users/currentUser/`;

      const data = await apiService(get_user_url, "GET");
      const requestUser = data["username"]
      window.localStorage.setItem("username", requestUser);

    }
  },

  mounted: function(){
    this.setUserInfo()
  }
};
</script>

<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
