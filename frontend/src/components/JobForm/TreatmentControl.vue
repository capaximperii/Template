<template>
  <v-container>
    <v-form ref="form" v-model="valid" lazy-validation>
      <v-text-field
        autofocus
        v-model="value.job_title"
        label="Job Title"
        :rules="required"
      />
      <v-text-field
        v-model="value.control_name"
        label="Control Name"
        :rules="required"
      />
      <v-text-field
        v-model="value.treatment_name"
        label="Treatment Name"
        :rules="required"
      />
      <v-select
        label="Submit Type"
        v-model="value.submit_type"
        :items="['hddsn', 'hddtrial', 'csv']"
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
