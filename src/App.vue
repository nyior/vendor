<template>
  <div id="app">
    <div class="margin-bottom">
      <NavbarComponent :hide_nav_brand="hide_nav_brand" :title="title" />

      <router-view />
    </div>

    <FooterComponent v-if="show_footer" />
  </div>
</template>

<script>
import NavbarComponent from "@/components/Navigation/Navbar.vue";
import FooterComponent from "@/components/Navigation/Footer.vue";

import { apiService } from "@/common/api.service.js";

export default {
  name: "App",
  components: {
    NavbarComponent,
    FooterComponent
  },

  data() {
    return {
      is_authenticated: null,
      show_footer: true,
      hide_nav_brand: false,
      title: null
    };
  },

  methods: {
    async setUserInfo() {
      let get_user_url = `api/v1/users/currentUser/`;

      const data = await apiService(get_user_url, "GET");
      const requestUser = data["username"];
      const requestUserStatus = data["authenticated"];
      const requestUserId = data["user_id"];

      this.is_authenticated = data["authenticated"];

      window.localStorage.setItem("username", requestUser);
      window.localStorage.setItem("authenticated", requestUserStatus);
      window.localStorage.setItem("user_id", requestUserId);

      console.log(data);
    },

    hideFooter() {
      this.show_footer = false;
    }
  },

  watch: {
    $route: function(value) {
      if (value.meta.hideFooter) {
        this.show_footer = false;
        this.hide_nav_brand = true;
        this.title = value.meta.title;
      } else {
        this.show_footer = true;
        this.hide_nav_brand = false;
        this.title = null;
      }
    }
  },

  created() {
    this.setUserInfo();
  }
};
</script>

<style>
#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
