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

    <!--  -->

    <div class="columns-is-multiline">
      <div class="column is-12">
        <h2 class="is-size-2 has-text-centered">LATEST LISTINGS</h2>
      </div>

      <div class="container">
        <div class="row align-center">
          <div
            class="column is-4 is-mobile"
            v-for="listings in latestListings"
            v-bind:key="listings.id"
          >
            <div class="box">
              <figure class="image mb-4">
                <img v-bind:src="listings.get_thumbnail" />
              </figure>

              <h3 class="is-size-4 has-text-centered">{{ listings.name }}</h3>
              <p class="is-size-6 has-text-grey has-text-centered">
                ${{ listings.price }}
              </p>
              <router-link
                v-bind:to="listings.get_absolute_url"
                class="button is-dark mt-4 box has-text-centered"
                >View details</router-link
              >
            </div>
          </div>
        </div>
      </div>

      <!-- <div
        class="column is-4 is-mobile"
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
            >View details</router-link
          >
        </div>
      </div> -->

      <!-- <ListingsBox
        v-for="listings in latestListings"
        v-bind:key="listings.id"
        v-bind:listings="listings"
      /> -->
    </div>
  </div>
</template>

<script>
import axios from "axios";
import ListingsBox from "../components/ListingsBox.vue";

export default {
  name: "HomeView",
  data() {
    return {
      latestListings: [],
    };
  },
  components: {
    ListingsBox,
  },

  mounted() {
    this.getLatestListings();

    document.title = "Home | REA";
  },
  methods: {
    async getLatestListings() {
      this.$store.commit("setIsLoading", true);

      await axios
        .get("/api/v1/latest-listings/")
        .then((response) => {
          this.latestListings = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
  },
};
</script>
