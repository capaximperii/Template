<template>
  <div>
    <Header title="Administration" :crumbs="crumbs" />
    <v-container>
      <v-row>
        <v-col cols="4" v-for="(l, i) in links" :key="i">
          <v-card class="mt-4" height="100%">
            <v-card-title>
              {{ l.title }}
              <v-spacer />
              <v-icon large :color="l.color">{{ l.icon }}</v-icon>
            </v-card-title>
            <v-card-subtitle class="mt-4">
              {{ l.detail }}
            </v-card-subtitle>
            <v-card-actions>
              <v-spacer />
              <v-btn :color="l.color" text :to="l.route">
                View
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>
<script>
import Header from "../components/Header";

export default {
  name: "Administration",
  components: {
    Header
  },
  data: () => ({
    show: false,
    links: [
      {
        title: "Downloads",
        detail: "Download monthly stats as excel and fetched logs.",
        icon: "mdi-download",
        color: "secondary",
        route: "Downloads"
      },
      {
        title: "Server Health",
        detail: "Monitor Server health in real time.",
        icon: "mdi-heart-pulse",
        color: "red darken-2",
        route: "Health"
      },
      {
        title: "Help",
        detail: "Get online help and documentation.",
        icon: "mdi-help",
        color: "success darken-2",
        route: "Help"
      }
    ],
    crumbs: [
      {
        text: "Dashboard",
        exact: true,
        disabled: false,
        to: {
          name: "Dashboard"
        }
      },
      {
        text: "Administration",
        exact: true,
        disabled: true,
        to: {
          name: "Administration"
        }
      }
    ]
  })
};
</script>
