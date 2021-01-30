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
  }
};
</script>

<style></style>
