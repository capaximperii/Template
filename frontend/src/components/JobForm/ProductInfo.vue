<template>
  <v-container>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        autofocus
        v-model.number="value.analytics_level"
        label="Analytics Level"
      />
      <v-text-field v-model="value.product" label="Product" :rules="required" />
      <v-text-field
        v-model="value.target_data"
        label="Target Data"
        :rules="required"
      />
      <v-col class="text-right">
        <v-btn color="primary" @click="handleInput">
          Continue
        </v-btn>
      </v-col>
    </v-form>
  </v-container>
</template>

<script>
export default {
  props: {
    value: {
      type: Object,
      required: true
    }
  },
  data: () => ({
    valid: false,
    required: [
      value => !!value || "Required.",
      value => (value && value.length >= 3) || "Min 3 characters"
    ]
  }),
  methods: {
    handleInput() {
      if (this.$refs.form.validate()) {
        this.$emit("input", this.value);
      }
    }
  }
};
</script>
