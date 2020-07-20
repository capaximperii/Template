<template>
  <div>
    <Header title="Home" :crumbs="crumbs" />
    <v-stepper v-model="activeStep">
      <v-stepper-header>
        <v-stepper-step :complete="activeStep > 1" step="1"
          >Treatment and Control</v-stepper-step
        >
        <v-divider></v-divider>

        <v-stepper-step :complete="activeStep > 2" step="2"
          >Product Info</v-stepper-step
        >
        <v-divider></v-divider>

        <v-stepper-step :complete="activeStep > 3" step="3"
          >Categorical Matching</v-stepper-step
        >
        <v-divider></v-divider>

        <v-stepper-step :complete="activeStep > 4" step="4"
          >Parametric Matching</v-stepper-step
        >
      </v-stepper-header>

      <v-stepper-items>
        <v-stepper-content step="1">
          <TreatmentControl :value="job" @input="activeStep = 2" />
        </v-stepper-content>

        <v-stepper-content step="2">
          <ProductInfo :value="job" @input="activeStep = 3" />
        </v-stepper-content>

        <v-stepper-content step="3">
          <CategoricalMatching :value="job" @input="activeStep = 4" />
        </v-stepper-content>

        <v-stepper-content step="4">
          <ParametricMatching :value="job" @input="submit" />
        </v-stepper-content>
      </v-stepper-items>
    </v-stepper>
  </div>
</template>

<script>
// @ is an alias to /src
import Header from "../components/Header";
import Job from "../models/job";

import TreatmentControl from "../components/JobForm/TreatmentControl";
import ProductInfo from "../components/JobForm/ProductInfo";
import CategoricalMatching from "../components/JobForm/CategoricalMatching";
import ParametricMatching from "../components/JobForm/ParametricMatching";

export default {
  name: "Home",
  components: {
    Header,
    TreatmentControl,
    ProductInfo,
    CategoricalMatching,
    ParametricMatching
  },
  data() {
    return {
      dashboard: [],
      activeStep: 1,
      crumbs: [
        {
          text: "Jobs",
          exact: true,
          disabled: true,
          to: {
            name: "Jobs"
          }
        }
      ],
      job: new Job()
    };
  },
  methods: {
    async submit() {
      await this.$http.post(`${this.baseUrl}/api/jobs`, this.job);
      this.$router.push("Reports");
    }
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
}
</style>
