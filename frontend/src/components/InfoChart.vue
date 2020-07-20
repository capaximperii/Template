<template>
  <v-card class="mx-auto" :color="color" width="100%">
    <v-card-title>
      <v-row align="center">
        <div class="caption text-uppercase text-right mr-4">
          {{ title }}
        </div>
        <div>
          <span class="display-2 font-weight-black" v-text="avg || '—'"></span>
          <strong v-if="avg">{{ units }}</strong>
        </div>
      </v-row>
    </v-card-title>

    <v-sheet color="transparent">
      <v-sparkline
        :smooth="16"
        :gradient="['purple', 'violet']"
        :line-width="3"
        :fill="true"
        :value="heartbeats"
        stroke-linecap="round"
      ></v-sparkline>
    </v-sheet>
  </v-card>
</template>
<script>
export default {
  props: {
    title: {
      type: String,
      default: ""
    },
    color: {
      type: String,
      default: "black"
    },
    units: {
      type: String,
      default: ""
    },
    data: {
      type: Array
    },
    field: {
      type: String,
      default: ""
    }
  },
  computed: {
    heartbeats() {
      return this.data.map(d => d[this.field]);
    },
    avg() {
      // const sum = this.heartbeats.reduce((acc, cur) => acc + cur, 0);
      // const length = this.heartbeats.length;
      // if (!sum && !length) return 0;
      // return Math.ceil(sum / length);
      return Math.ceil(this.heartbeats[0]);
    }
  }
};
</script>
