import { UserManager } from "oidc-client";
import config from "../config";
import Vue from "vue";

let Auth = {
  install(Vue) {
    let oauthIdentity = new UserManager({
      ...config.auth,
      monitorSession: false
    });
    console.log("Installing Identify plugins.");

    Vue.prototype.OauthLogin = async () => {
      await oauthIdentity.signinRedirect();
    };

    Vue.prototype.OauthLogout = async () => {
      await oauthIdentity.signoutRedirect();
    };

    Vue.prototype.oauthIdentity = oauthIdentity;
  }
};

Vue.use(Auth);
