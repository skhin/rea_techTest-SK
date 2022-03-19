<template>
  <div class="page-search">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Search</h1>
        <h2 class="is-size-5 has-text-grey">Searching for: "{{ query }}"</h2>
      </div>

      <ListingsBox
        v-for="listings in listings"
        v-bind:key="listings.id"
        v-bind:listings="listings"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ListingsBox from "../components/ListingsBox.vue";

export default {
  name: "Search",
  components: {
    ListingsBox,
  },
  data() {
    return {
      listings: [],
      query: "",
    };
  },
  mounted() {
    document.title = "Search | Djackets";
    let uri = window.location.search.substring(1);
    let params = new URLSearchParams(uri);
    if (params.get("query")) {
      this.query = params.get("query");
      this.performSearch();
    }
  },
  methods: {
    async performSearch() {
      this.$store.commit("setIsLoading", true);
      await axios
        .post("/api/v1/listings/search/", { query: this.query })
        .then((response) => {
          this.listings = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
