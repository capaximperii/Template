<template>
  <div>
    <Header title="Home" :crumbs="crumbs" />
    <v-container class="mt-0 pt-0"> </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header";

export default {
  name: "Home",
  components: {
    Header
  },
  data() {
    return {
      dashboard: [],
      key: 0,
      crumbs: [
        {
          text: "Home",
          exact: true,
          disabled: true,
          to: {
            name: "Home"
          }
        }
      ]
    };
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
}
</style>
