<template>
  <v-container>
    <v-form ref="form" v-model="valid" lazy-validation>
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
    valid: false
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
