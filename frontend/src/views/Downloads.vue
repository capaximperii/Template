<template>
  <div>
    <Header title="Downloads" :crumbs="crumbs" />
    <v-container>
      <v-row>
        <v-col cols="2" v-for="(l, i) in filteredResults" :key="i">
          <v-card flat class="text-center">
            <v-icon size="100" v-if="l.type == 'dir'" @click="chdir(l.name)"
              >mdi-folder</v-icon
            >
            <div v-else>
              <div align="end">
                <v-icon small color="error darken-2" @click="remove(l.name)"
                  >mdi-delete</v-icon
                >
              </div>

              <v-icon size="100" color="primary lighten-2" @click="fetchFile(l)"
                >mdi-file</v-icon
              >
            </div>
            <p class="font-weight-bold text-center">{{ l.name }}</p>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Header from "../components/Header";

export default {
  name: "Downloads",
  components: {
    Header
  },
  data: () => ({
    path: "",
    files: [],
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
        text: "Downloads",
        exact: true,
        disabled: true,
        to: {
          name: "Downloads"
        }
      }
    ]
  }),
  computed: {
    filteredResults() {
      return this.files;
    }
  },
  async mounted() {
    this.path = this.$route.query.path || "";
    await this.listFiles();
  },
  methods: {
    async chdir(p) {
      this.path = p;
      await this.listFiles();
    },
    async remove(p) {
      const params = encodeURIComponent(
        encodeURIComponent(`${this.path}/${p}`)
      );
      await this.$http.delete(`${this.baseUrl}/api/downloads/${params}`);
      await this.listFiles();
    },
    async listFiles() {
      const params = {
        path: this.path
      };
      let files = await this.$http.get(`${this.baseUrl}/api/downloads`, {
        params
      });
      this.files = files.data;
    },
    async fetchFile(l) {
      let target = `${this.baseUrl}/api/downloads/${l.name}?path=${l.path}`;
      window.open(target, "_blank");
    }
  }
};
</script>
