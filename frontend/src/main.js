import Vue from "vue";
import router from "./router";
import store from "./store";
import vuetify from "./plugins/vuetify";
import "roboto-fontface/css/roboto/roboto-fontface.css";
import "@mdi/font/css/materialdesignicons.css";
import "axios-progress-bar/dist/nprogress.css";

import "./plugins/http";
import {} from "./plugins/auth";
import App from "./App.vue";

Vue.prototype.baseUrl = process.env.VUE_APP_DASHBOARD_API_URL;
Vue.prototype.VUE_APP_VERSION = process.env.VUE_APP_VERSION;

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount("#app");
