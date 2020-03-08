import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Adverts from "./views/Adverts.vue";
import AdvertCreate from "./views/AdvertCreate.vue";
import AdvertDetail from "./views/AdvertDetail.vue";
import UserDetail from "./views/UserDetail.vue";


Vue.use(Router);

export default new Router({
  mode: "history",

  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },

    {
      path: "/ad_detail/:slug",
      name: "ad_detail",
      component: AdvertDetail,
      props: true
    },

    {
      path: "/user_detail/:id",
      name: "user_detail",
      component: UserDetail,
      props: true
    },
    {
      path: "/ads_create",
      name: "ads_create",
      component: AdvertCreate
    },
    {
      path: "/adverts",
      name: "adverts",
      component: Adverts
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      //component: () =>
      // import(/* webpackChunkName: "about" */ "./views/Adverts.vue")
    }
  ]
});
