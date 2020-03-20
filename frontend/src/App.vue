<template>
  <div id="app">
    <NavbarComponent 
          :authenticated="is_authenticated"
        
    />
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

  data(){
    return{
      is_authenticated: null,
    
    }
  },

  methods: {
    async setUserInfo(){
      let get_user_url = `api/v1/users/currentUser/`;

      const data = await apiService(get_user_url, "GET");
      const requestUser = data["username"];
      const requestUserStatus = data["authenticated"];
      const requestUserId = data["user_id"];

      this.is_authenticated = data["authenticated"];
    

      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("authenticated", requestUserStatus);
      window.localStorage.setItem("user_id", requestUserId);

    },
  },

  created(){
    this.setUserInfo();
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
