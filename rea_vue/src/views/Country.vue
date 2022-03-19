<template>
  <div class="page-country">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">{{ country.name }}</h2>
      </div>

      <div
        class="column-is-3"
        v-for="listings in country.listings"
        v-bind:key="listings.id"
      >
        <div class="box">
          <figure class="image mb-4">
            <img v-bind:src="listings.get_thumbnail" />
          </figure>

          <h3 class="is-size-4">{{ listings.name }}</h3>
          <p class="is-size-6 has-text-grey">${{ listings.price }}</p>

          <router-link
            v-bind:to="listings.get_absolute_url"
            class="button is-dark mt-4"
          >
            View Details</router-link
          >
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";
export default {
  name: "Country",
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
