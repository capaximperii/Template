<template>
  <v-banner single-line :sticky="true" class="accent darken-4">
    <template v-slot:default>
      <v-breadcrumbs class="ml-4 pl-4" :items="crumbs" large></v-breadcrumbs>
    </template>
    <template v-slot:actions>
      <UserMenu />
    </template>
  </v-banner>
</template>
<script>
import UserMenu from "./UserMenu";

export default {
  components: {
    UserMenu
  },
  props: {
    title: {
      type: String,
      default: "Home"
    },
    crumbs: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      query: "",
      inverted: false
    };
  }
};
</script>
<style scoped>
.v-banner--single-line {
  z-index: 9 !important;
}
</style>
