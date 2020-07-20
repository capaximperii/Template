<template>
  <div>
    <Header title="Help" :crumbs="crumbs" />
    <v-tabs icons-and-text grow>
      <v-tab>
        <v-icon left>mdi-information</v-icon>
        About
      </v-tab>
      <v-tab>
        <v-icon left>mdi-layers</v-icon>
        Database
      </v-tab>
      <v-tab>
        <v-icon left>mdi-help</v-icon>
        FAQ
      </v-tab>
      <v-tab-item>
        <Editor mode="viewer" nativeEmoji :outline="false" v-model="about" />
      </v-tab-item>
      <v-tab-item>
        <Editor mode="viewer" nativeEmoji :outline="false" v-model="database" />
      </v-tab-item>
      <v-tab-item>
        <Editor
          mode="viewer"
          nativeEmoji
          :outline="false"
          :preview="true"
          v-model="help"
        />
      </v-tab-item>
    </v-tabs>
  </div>
</template>
<script>
import { Editor } from "vuetify-markdown-editor";
import Header from "../components/Header";
import About from "../../../README.md";
import Database from "../../../documents/Database.md";
import Help from "../../../documents/Help.md";

export default {
  name: "help",
  components: {
    Editor,
    Header
  },
  data() {
    return {
      about: About,
      help: Help,
      database: Database,
      crumbs: [
        {
          text: "Home",
          exact: true,
          disabled: false,
          to: {
            name: "Home"
          }
        },
        {
          text: "Help",
          exact: true,
          disabled: true,
          to: {
            name: "Help"
          }
        }
      ]
    };
  }
};
</script>
<style>
div.markdown-text table tr td {
  border: 1px solid;
  padding-right: 10px;
  padding-left: 10px;
}
div.markdown-text table th {
  border: 2px solid;
  padding-right: 10px;
  padding-left: 10px;
}
</style>
