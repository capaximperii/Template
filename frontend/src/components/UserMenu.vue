<template>
  <div class="text-center">
    <v-menu offset-y>
      <template v-slot:activator="{ on, attrs }">
        <v-btn depressed v-bind="attrs" v-on="on">
          {{ DisplayName }}
          <v-icon>mdi-account</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item @click="OauthLogin()" v-if="!Authenticated">
          <v-list-item-title>Login</v-list-item-title>
        </v-list-item>
        <EditUser v-if="Authenticated" />
        <v-list-item @click="OauthLogout()" v-if="Authenticated">
          <v-list-item-title>Logout</v-list-item-title>
        </v-list-item>
      </v-list>
    </v-menu>
  </div>
</template>
<script>
import { mapGetters } from "vuex";
import EditUser from "../popups/EditUser";

export default {
  components: {
    EditUser
  },
  data: () => ({}),
  computed: {
    ...mapGetters(["DisplayName", "Authenticated"])
  },
  methods: {
    async FetchUser() {
      this.oauthIdentity.getUser().then(user => {
        console.log(user);
      });
    }
  }
};
</script>
