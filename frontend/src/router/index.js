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

      children: [
        {
          path: "",
          name: "join",
          components: JoinMarche 
        }
      ],
        
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

      children: [
        {
          path: "",
          name: "join",
          component: JoinMarche
        }
      ],

      // meta: {
      //   requiresAuth: true,
      // },

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

      children: [
        {
          path: " ",
          name: "join",
          components: {
            JoinMarche
          }
        }
      ],

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

// router.beforeEach((to, from, next) => {
//   var isAuthenticated = JSON.parse(window.localStorage.getItem("authenticated"));

//   if (to.matched.some(route => route.meta.requiresAuth)) {

//     if (isAuthenticated) {

//       next();

//     } else { 

//       next({
//         name: "join" // back to safety route //
//       });
      
//     }
    
//   }

//   next();
// });

export default router;