<template>
  <div>
    <Header title="Reports" :crumbs="crumbs" />
    <GenericTable
      :headers="headers"
      :pageful="pageful"
      :search="search"
      title="Jobs List"
      @input="fetchPageful"
    />
  </div>
</template>
<script>
import Header from "../components/Header";
import GenericTable from "../components/GenericTable";

export default {
  name: "Reports",
  components: {
    Header,
    GenericTable
  },
  data: () => ({
    search: { page: 1 },
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
        text: "Jobs",
        exact: true,
        disabled: true,
        to: {
          name: "Jobs"
        }
      }
    ],
    headers: [
      { text: "Id", value: "id", align: "center" },
      { text: "Status", value: "status", align: "center" },
      { text: "Title", value: "job_title", align: "center" },
      { text: "Requester", value: "Users.name", align: "center" },
      { text: "Department", value: "Users.department", align: "center" },
      { text: "Email", value: "Users.email", align: "center" },
      { text: "Submitted", value: "created", align: "center" }
    ],
    pageful: {
      page: 1,
      total: 1,
      items: []
    }
  }),
  methods: {
    async fetchPageful(val) {
      const params = { ...val };
      let pageful = await this.$http.get(`${this.baseUrl}/api/jobs`, {
        params
      });
      pageful.data.items.map(
        f => (f.created = new Date(f.created + "Z").toLocaleString("en-US"))
      );
      this.pageful = pageful.data;
    }
  }
};
</script>
