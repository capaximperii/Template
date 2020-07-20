<template>
  <div>
    <Header title="Home" :crumbs="crumbs" />
    <v-row class="mx-4" no-gutter>
      <v-col cols="3">
        <InfoChart
          title="Server Process Mem "
          color="blue-grey lighten-4"
          units=" %"
          :data="healthData"
          field="mempc"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="CPU "
          color="blue-grey lighten-3"
          units=" %"
          :data="healthData"
          field="cpu"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="Network connections "
          color="blue-grey lighten-2"
          units=""
          :data="healthData"
          field="net"
        />
      </v-col>
      <v-col cols="3">
        <InfoChart
          title="Memory Available "
          color="blue-grey lighten-1"
          units=" %"
          :data="healthData"
          field="memtotal"
        />
      </v-col>
    </v-row>
    <v-container class="mt-0 pt-0">
      <v-row dense>
        <v-col cols="12">
          <v-card color="#1F7087" dark>
            <v-card-title class="headline"
              >Current version:
              <i class="ml-3">
                {{ healthData[0].version }}
              </i>
              <v-row justify="end">
                <v-col cols="4" offset="5" v-if="false === checkedForUpdate">
                  <v-btn class="ma-0 pa-0" text @click="checkUpdate">
                    Check now <v-icon class="ml-1">mdi-update</v-icon>
                  </v-btn>
                </v-col>
                <v-col cols="6" v-else>
                  <v-row>
                    <v-col cols="6">
                      <v-select
                        class="ma-0 pa-0"
                        :items="updates.releases"
                        :label="updates.version"
                        v-model="selectedVersion"
                      >
                      </v-select>
                    </v-col>
                    <v-col cols="4">
                      <v-btn
                        :disabled="selectedVersion === null"
                        :loading="upgrading"
                        color="secondary"
                        @click="doUpdate"
                      >
                        Upgrade
                      </v-btn>
                    </v-col>
                  </v-row>
                </v-col>
              </v-row>
            </v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Vue from "vue";
import Header from "../components/Header";
import InfoChart from "../components/InfoChart";

export default {
  name: "Home",
  components: {
    Header,
    InfoChart
  },
  data() {
    return {
      dead: false,
      upgrading: false,
      checkedForUpdate: false,
      healthData: [],
      updates: null,
      selectedVersion: null,
      crumbs: [
        {
          text: "Administration",
          exact: true,
          disabled: false,
          to: {
            name: "Administration"
          }
        },
        {
          text: "Health",
          exact: true,
          disabled: true,
          to: {
            name: "Health"
          }
        }
      ]
    };
  },
  async created() {
    for (let i = 0; i < 20; i++) {
      this.healthData.unshift({
        cpu: 0,
        mempc: 0,
        net: 0,
        memtotal: 0,
        version: "Development"
      });
    }
    Vue.nextTick(this.pollHealth);
  },
  methods: {
    async checkUpdate() {
      const response = await this.$http.put(`${this.baseUrl}/api/health`);
      this.updates = response.data;
      this.checkedForUpdate = true;
    },
    async doUpdate() {
      this.upgrading = true;
      let payload = {
        version: this.selectedVersion
      };
      try {
        const response = await this.$http.post(
          `${this.baseUrl}/api/health`,
          payload
        );
        this.updates = response.data;
      } catch (err) {
        /* eslint-disable no-unused-vars */
        this.$router.go(); // Reload
        /* eslint-enable no-unused-vars */
      } finally {
        this.upgrading = false;
      }
    },
    async pollHealth() {
      for (;;) {
        if (this.dead) break;
        const response = await this.$http.get(`${this.baseUrl}/api/health`);
        this.healthData.unshift(response.data);
        await new Promise(resolve => setTimeout(resolve, 10000));
        this.healthData.length = 20;
      }
    }
  },
  destroyed() {
    this.dead = true;
  }
};
</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
a {
  text-decoration: none;
}
</style>
