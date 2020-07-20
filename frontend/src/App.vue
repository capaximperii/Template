<template>
  <v-app>
    <Drawer />
    <v-content>
      <router-view></router-view>
    </v-content>
  </v-app>
</template>

<script>
import Drawer from "./components/Drawer";

export default {
  name: "App",
  components: {
    Drawer
  },
  data() {
    return {};
  },
  async mounted() {
    await this.$store.dispatch("FetchUserInfo");
  }
};
</script>
<style>
::-webkit-scrollbar {
  width: 3px;
  height: 3px;
}
::-webkit-scrollbar-track {
  background: white;
}
::-webkit-scrollbar-thumb {
  background: #ddd;
  visibility: hidden;
}
::-webkit-scrollbar-thumb {
  visibility: visible;
}
.v-breadcrumbs__item--disabled {
  font-weight: 1000 !important;
  font-size: 2em;
}
</style>
