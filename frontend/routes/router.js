import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import ReviewEditor from "./views/ReviewEditor.vue";
import Adverts from "./views/Adverts.vue";
import AdvertCreate from "./views/AdvertCreate.vue";
import AdvertDetail from "./views/AdvertDetail.vue";
import UserDetail from "./views/UserDetail.vue";
import Wishlist from "./views/Wishlist.vue";
import Category from "./views/Category.vue";
import SearchView from "./views/SearchView.vue";


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
      path: "/wishlist",
      name: "wishlist",
      
      component: Wishlist,
      meta: {
        requiresAuth: true,
      },
    },

    {
      path: "/ad_detail/:slug",
      name: "ad_detail",
      component: AdvertDetail,
      props: true
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
      props: true,
      meta: {
        requiresAuth: true,
      },
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
      
      props: true,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: "/review/:id",
      name: "edit_review",
      component: ReviewEditor,
      props: true
    },
    {
      path: "/adverts",
      name: "adverts",
      component: Adverts
      
    }
  ]
});

router.beforeEach((to, from, next) => {
  var check = true;

  if (to.matched.some(route => route.meta.requiresAuth)) {

    if (window.localStorage.getItem("authenticated") === "true") {
      next();
    } else {
      
      next('/');
    }
    
  }
  next();
});

export default router;