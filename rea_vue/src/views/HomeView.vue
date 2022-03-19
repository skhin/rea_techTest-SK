<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-6">
          Welcome to REAL ESTATE ANALYTICS PROPERTY LISTINGS
        </p>
        <p class="tagline">The fatest way to get your dream property</p>
      </div>
    </section>

    <div class="columns-is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">LATEST LISTINGS</h2>
      </div>
    </div>

    <div
      class="column-is-3"
      v-for="listings in latestListings"
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
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      latestListings: [],
    };
  },
  components: {},

  mounted() {
    this.getLatestListings();
  },
  methods: {
    getLatestListings() {
      axios
        .get("/api/v1/latest-listings/")
        .then((response) => {
          this.latestListings = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style scoped>
.image {
  margin-top: -1.25rem;
  margin-left: -1.25rem;
  margin-right: -1.25rem;
  width: 300px;
}
</style>
