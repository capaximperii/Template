<template>
  <v-dialog v-model="dialog" width="70%">
    <template v-slot:activator="{ on }">
      <v-list-item v-on="on">
        <v-list-item-title>Profile</v-list-item-title>
      </v-list-item>
    </template>
    <v-card justify="center" v-if="null !== user">
      <v-card-title class="headline">User Profile</v-card-title>
      <v-form ref="form">
        <v-col cols="10" offset="1">
          <v-row no-gutter>
            <v-col cols="10" offset="0">
              <v-text-field readonly label="Name" v-model="user.name" />
            </v-col>
            <v-col cols="10" offset="0">
              <v-text-field readonly label="Email" v-model="user.email" />
            </v-col>
            <v-col cols="8">
              <v-select
                v-model="user.department"
                :items="['Department A', 'Department B', 'OTHERS']"
                label="Department"
              ></v-select>
            </v-col>
          </v-row>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="primary" text @click="validate_and_save">
              Save
            </v-btn>
            <v-btn color="error" text @click="dialog = false">
              Close
            </v-btn>
          </v-card-actions>
        </v-col>
      </v-form>
    </v-card>
  </v-dialog>
</template>
<script>
export default {
  components: {},
  data: () => ({
    dialog: false,
    user: null
  }),
  async mounted() {
    let u = await this.$http.get(`${this.baseUrl}/api/users`);
    this.user = u.data;
  },
  methods: {
    async validate_and_save() {
      if (this.$refs.form.validate()) {
        await this.$http.put(`${this.baseUrl}/api/users`, this.user);
        this.dialog = false;
        this.$emit("input");
      }
    }
  }
};
</script>
