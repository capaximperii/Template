<template>
  <v-card>
    <v-card-title>
      {{ title }}
      <v-spacer />
      <v-col cols="2">
        <v-text-field
          v-model="search.query"
          append-icon="mdi-magnify"
          placeholder="Filter"
        >
        </v-text-field>
      </v-col>
    </v-card-title>
    <v-data-table
      :headers="headers"
      :items="pageful.items"
      :options.sync="options"
      :multi-sort="false"
      hide-default-footer
      pa-4
      fixed-header
      disable-pagination
    >
    </v-data-table>
    <v-pagination v-model="search.page" :length="pageful.pages"></v-pagination>
  </v-card>
</template>

<script>
import _ from "lodash";

export default {
  name: "GenericTable",
  props: {
    headers: {
      type: Array,
      default: () => []
    },
    pageful: {
      type: Object,
      default: () => {
        return {
          items: [],
          total: 1,
          page: 1
        };
      }
    },
    title: {
      type: String,
      default: "Unknown"
    },
    search: {
      type: Object,
      default: () => {
        return { page: 1 };
      }
    }
  },
  data() {
    return {
      options: {}
    };
  },
  methods: {
    debounced: _.debounce(function(val) {
      let query = {
        query: this.search.query,
        page: val.page,
        column: this.options.sortBy[0],
        order: this.options.sortDesc[0] ? "desc" : "asc"
      };
      this.$emit("input", query);
    }, 1000)
  },
  watch: {
    search: {
      handler: "debounced",
      deep: true,
      immediate: false
    },
    options: {
      handler: "debounced",
      deep: true,
      immediate: false
    }
  }
};
</script>
