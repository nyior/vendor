import Vue from "vue";
import App from "./App.vue";
import router from "./router/index";
import "./registerServiceWorker";
import { store } from "./store/store";
import VeeValidate from 'vee-validate';

Vue.use(VeeValidate);

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
