import Vue from "vue";
import Vuetify from "vuetify/lib";
import { Ripple, Touch } from "vuetify/lib/directives";
import { VSnackbar, VBtn, VIcon, VCheckbox, VSelect } from "vuetify/lib";
import {
  VContainer,
  VRow,
  VCol,
  VCard,
  VToolbar,
  VHover,
  VDivider,
  VTextarea
} from "vuetify/lib";

Vue.use(Vuetify, {
  components: {
    VSnackbar,
    VBtn,
    VIcon,
    VCheckbox,
    VSelect,
    VContainer,
    VRow,
    VCol,
    VCard,
    VHover,
    VToolbar,
    VDivider,
    VTextarea
  },
  directives: {
    Ripple,
    Touch
  }
});

export default new Vuetify({
  theme: {
    dark: false
  }
});
