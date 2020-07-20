<template>
  <div>
    <v-app>
      <v-layout v-cloak style="padding-top:30vh">
        <v-flex v-if="!errorMessage">
          <div class="text-sm-center">
            <v-progress-circular
              :size="70"
              :width="7"
              indeterminate
              color="primary"
            />
          </div>
          <div class="text-sm-center">
            Logging you in...
          </div>
        </v-flex>
        <v-flex v-else>
          {{ errorMessage }}
        </v-flex>
      </v-layout>
    </v-app>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      errorMessage: null
    };
  },
  mounted() {
    this.signinRedirect();
  },
  methods: {
    async signinRedirect() {
      await this.oauthIdentity.clearStaleState(null);
      let identity = await this.oauthIdentity.signinRedirectCallback(null);
      await this.$store.dispatch("FetchUserInfo");
      axios.defaults.headers.common = {
        Authorization: `Bearer ${identity.id_token}`
      };
      let redirectUrl = localStorage.getItem("redirectUrl") || "Home";
      console.log("redirect  " + redirectUrl);
      this.$router.replace(redirectUrl);
    }
  }
};
</script>

<style>
[v-cloak] {
  display: none !important;
}
</style>
