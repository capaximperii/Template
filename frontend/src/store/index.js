import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    authUser: null
  },
  mutations: {
    SetAuthUser(state, value) {
      state.authUser = value;
      let id_token = value == null ? "" : value.id_token;
      axios.defaults.headers.common = {
        Authorization: `Bearer ${id_token}`
      };
    }
  },
  actions: {
    async FetchUserInfo({ commit }) {
      let u = await Vue.prototype.oauthIdentity.getUser();
      commit("SetAuthUser", u);
    }
  },
  getters: {
    DisplayName: state => {
      return state.authUser ? state.authUser.profile.name : "Guest";
    },
    Authenticated: state => {
      return state.authUser !== null;
    }
  },
  modules: {}
});
