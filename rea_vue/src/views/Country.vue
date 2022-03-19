<template>
  <div class="page-country">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ country.name }}</h2>
      </div>

      <ListingsBox
        v-for="listings in country.listings"
        v-bind:key="listings.id"
        v-bind:listings="listings"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
import ListingsBox from "../components/ListingsBox.vue";

export default {
  name: "Country",
  components: {
    ListingsBox,
  },
  data() {
    return {
      country: {
        listings: [],
      },
    };
  },
  mounted() {
    this.getCountry();
  },
  watch: {
    $route(to, from) {
      if (to.name === "Country") {
        this.getCountry();
      }
    },
  },
  methods: {
    async getCountry() {
      const countrySlug = this.$route.params.country_slug;
      this.$store.commit("setIsLoading", true);

      await axios
        .get(`/api/v1/listings/${countrySlug}/`)
        .then((response) => {
          this.country = response.data;

          document.title = this.country.name + " | REA";
        })
        .catch((error) => {
          console.log(error);
        });

      toast({
        message: "Something went wrong. Please try again",
        type: "is-danger",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
      });

      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
