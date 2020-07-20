import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home";
import Downloads from "../views/Downloads";
import Jobs from "../views/Jobs";
import Reports from "../views/Reports";
import Login from "../views/Login";
import Logout from "../views/Logout";
import Administration from "../views/Administration";
import Health from "../views/Health";

const Help = () => import("../views/Help");

async function checkAuthentication(to, from, next) {
  let user = await Vue.prototype.oauthIdentity.getUser();
  if (null == user) Vue.prototype.OauthLogin();
  else next();
}

Vue.use(VueRouter);

const routes = [
  {
    path: "/Home",
    name: "Home",
    component: Home
  },
  {
    name: "Jobs",
    path: "/Jobs",
    component: Jobs,
    beforeEnter: checkAuthentication
  },
  {
    name: "Downloads",
    path: "/Downloads",
    component: Downloads,
    beforeEnter: checkAuthentication
  },
  {
    name: "Reports",
    path: "/Reports",
    component: Reports,
    beforeEnter: checkAuthentication
  },
  {
    name: "Administration",
    path: "/Administration",
    component: Administration,
    beforeEnter: checkAuthentication
  },
  {
    name: "Health",
    path: "/Health",
    component: Health,
    beforeEnter: checkAuthentication
  },
  {
    name: "Help",
    path: "/Help",
    component: Help
  },
  {
    name: "Login",
    path: "/LoginCallback",
    component: Login
  },
  {
    name: "Logout",
    path: "/LogoutCallback",
    component: Logout
  },
  {
    // This is a hack to use :to tag for absolute paths.
    path: "/http*",
    beforeEnter: to => {
      window.open(to.fullPath.substring(1), "_blank");
    }
  },
  { path: "*", redirect: "/Home" }
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes
});

export default router;
