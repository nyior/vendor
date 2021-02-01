import Vue from "vue";
import Router from "vue-router";

import Home from "@/views/Home/Home.vue";
import ReviewEditor from "@/views/Reviews/ReviewEditor.vue";
import Adverts from "@/views/Adverts/Adverts.vue";
import AdvertCreate from "@/views/Adverts/AdvertCreate.vue";
import AdvertDetail from "@/views/Adverts/AdvertDetail.vue";
import UserDetail from "@/views/User/UserDetail.vue";
import Wishlist from "@/views/Wishlist/Wishlist.vue";
import Category from "@/views/Category/Category.vue";
import SearchView from "@/views/Search/SearchView.vue";
import JoinMarche from "@/components/Modals/JoinMarche.vue";
import Continue from "@/views/Auth/Continue.vue";
import Login from "@/views/Auth/Login.vue";
import Register from "@/views/Auth/Register.vue";

Vue.use(Router);

const router = new Router({
  mode: "history",

  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },

    {
      path: "/login",
      name: "login",
      component: Login,
      meta: {
        hideFooter: true,
        title: "login"
      }
    },

    {
      path: "/register",
      name: "register",
      component: Register,
      meta: {
        hideFooter: true,
        title: "register"
      }
    },

    {
      path: "/continue",
      name: "continue",
      component: Continue,
      meta: {
        hideFooter: true,
        title: "continue"
      }
    },

    {
      path: "/wishlist",
      name: "wishlist",
      component: Wishlist

      // children: [
      //   {
      //     path: "",
      //     name: "join",
      //     components: JoinMarche
      //   }
      // ],
    },

    {
      path: "/ad_detail/:slug",
      name: "ad_detail",
      component: AdvertDetail,
      props: true,
      meta: { hideFooter: true }
    },

    {
      path: "/category/:category",
      name: "category",
      component: Category,
      props: true
    },

    {
      path: "/user_detail/:id",
      name: "user_detail",
      component: UserDetail,
      props: true
    },

    {
      path: "/search/:search_key?",
      name: "search",
      component: SearchView,
      props: true
    },

    {
      path: "/ads_create/:slug?",
      name: "ads_create",
      component: AdvertCreate,

      meta: { hideFooter: true, title: "sell on marche" },

      props: true

      // children: [
      //   {
      //     path: " ",
      //     name: "join",
      //     components: {
      //       JoinMarche
      //     }
      //   }
      // ]
    },

    {
      path: "/review/:id",
      name: "edit_review",
      component: ReviewEditor,
      meta: { hideFooter: true },
      props: true
    },

    {
      path: "/adverts",
      name: "adverts",
      component: Adverts
    }
  ]
});

// router.beforeEach((to, from, next) => {
//   let isAuthenticated = is_authenticated;

//   if (to.matched.some(route => route.meta.hideFooter)){

//     to.$emit('hide:footer');

//     next();

//   }

//   next();

// });

export default router;
