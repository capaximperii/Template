<template>
  <v-navigation-drawer
    app
    expand-on-hover
    :mini-variant="true"
    :permanent="true"
    dark
    class="accent darken-2"
  >
    <v-list dense nav>
      <v-list-item>
        <v-list-item-content>
          <v-list-item-title class="title">
            <v-icon
              :color="$vuetify.theme.dark ? 'lime accent-1' : 'orange accent-2'"
              class="mr-4 ml-0 pr-4 pl-0"
              @click="$vuetify.theme.dark = !$vuetify.theme.dark"
              >mdi-white-balance-sunny</v-icon
            >
            {{ VUE_APP_VERSION }}
          </v-list-item-title>
          <v-list-item-subtitle></v-list-item-subtitle>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list-item
        v-for="item in menuItems"
        :key="item.title"
        link
        :to="item.to"
      >
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <v-list-item-title>{{ item.title }}</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
    </v-list>

    <v-footer
      absolute
      padless
      class="text-center ma-0 pa-0 accent darken-2"
      max-height="25px"
    >
      © FooBar 2020
    </v-footer>
  </v-navigation-drawer>
</template>
<script>
import { mapState } from "vuex";

export default {
  data() {
    return {
      items: [
        {
          title: "Home",
          icon: "mdi-home",
          to: { name: "Home" },
          auth: false
        },
        {
          title: "Jobs",
          icon: "mdi-rocket",
          to: { name: "Jobs" },
          auth: true
        },
        {
          title: "Reports",
          icon: "mdi-format-list-numbered",
          to: { name: "Reports" },
          auth: true
        },
        {
          title: "Administration",
          icon: "mdi-key",
          to: { name: "Administration" },
          auth: true
        }
      ],
      right: null
    };
  },
  computed: {
    ...mapState(["authUser"]),
    menuItems() {
      if (this.authUser != null) {
        return this.items;
      }
      return this.items.filter(i => i.auth === false);
    }
  }
};
</script>
<style scoped>
.v-navigation-drawer--fixed {
  z-index: 10 !important;
}
</style>
