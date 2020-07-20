<template>
  <v-layout align-center justify-center wrap>
    <v-flex xs12 class="text-center">
      <v-icon size="400">mdi-shield-key</v-icon>
      <p class="pt-4 mt-4 display-3 font-weight-thin">
        You have been logged out.
      </p>
    </v-flex>
  </v-layout>
</template>

<script>
export default {
  data() {
    return {};
  },
  async mounted() {
    await this.oauthIdentity.clearStaleState(null);
    await new Promise(resolve => setTimeout(resolve, 2000));
    this.$router.replace("Home");
  }
};
</script>

<style></style>
