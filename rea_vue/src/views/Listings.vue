<template>
  <div class="listings-page">
    <div class="columns is-multiline">
      <div class="column is-9">
        <figure class="image mb-6">
          <img v-bind:src="listings.get_image" />
        </figure>

        <h1 class="title">{{ listings.name }}</h1>
        <p>{{ listings.description }}</p>
      </div>
      <div class="column is-3">
        <h2 class="subinfo">INFORMATION</h2>
        <p><strong>Price: </strong>${{ listings.price }}</p>

        <div class="field has-addons mt-6">
          <div class="control">
            <input type="number" min="1" class="input" v-model="quantity" />
          </div>
          <div class="control">
            Schedule a Call with Agent
            <a class="button is-dark">Agent Call</a>
          </div>

          <div class="control">
            <input type="number" min="1" class="input" v-model="quantity" />
          </div>
          <div class="control">
            Schedule a Visit with Agent
            <a class="button is-dark">Agent Visit</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Listings",
  data() {
    return {
      listings: {},
      quantity: 1,
    };
  },

  mounted() {
    this.getListings();
  },
  methods: {
    getListings() {
      const country_slug = this.$route.params.country_slug;
      const listings_slug = this.$route.params.listings_slug;

      axios
        .get(`/api/v1/listings/${country_slug}/${listings_slug}`)
        .then((response) => {
          this.listings = response.data;
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
  width: 700px;
}
</style>
