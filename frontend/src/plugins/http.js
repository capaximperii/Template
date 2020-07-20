import Vue from "vue";
import axios from "axios";
import VuetifyToast from "vuetify-toast-snackbar";
import { loadProgressBar } from "axios-progress-bar";

// First session key is user?
let identity = JSON.parse(sessionStorage.getItem(sessionStorage.key(0))) || {
  id_token: ""
};
axios.defaults.headers.common = {
  Authorization: `Bearer ${identity.id_token}`
};

axios.interceptors.response.use(
  response => {
    if (response.status === 202) {
      Vue.prototype.$toast.info("You request has been queued", {
        icon: "mdi-information",
        color: "green"
      });
    } else if (response.status === 201) {
      Vue.prototype.$toast.info("Operation successful", {
        icon: "mdi-check",
        color: "green"
      });
    }
    return response;
  },
  async error => {
    if (!error.response) {
      Vue.prototype.$toast.info("Server is down", {
        icon: "mdi-check",
        color: "green"
      });
    } else if (error.response.status === 400) {
      Vue.prototype.$toast.error("Bad or malformed request.", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status === 403) {
      Vue.prototype.$toast.error("Session has expired.", {
        icon: "mdi-alert-circle",
        color: "red"
      });
      await new Promise(resolve => setTimeout(resolve, 2000));
      Vue.prototype.OauthLogin();
    } else if (error.response.status === 409) {
      Vue.prototype.$toast.error("Cannot add duplicates in the system.", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status > 409 && error.response.status < 502) {
      Vue.prototype.$toast.error("Operation failed", {
        icon: "mdi-alert-circle",
        color: "red"
      });
    } else if (error.response.status === 502) {
      Vue.prototype.$toast.info("Server is down", {
        icon: "mdi-check",
        color: "green"
      });
    }
    return Promise.reject(error.response);
  }
);

loadProgressBar({ showSpinner: false });
Vue.prototype.$http = axios;
Vue.use(VuetifyToast, {
  x: "center",
  y: "top",
  dismissable: true,
  property: "$toast"
});
