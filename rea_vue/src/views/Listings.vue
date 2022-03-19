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
          Schedule a Visit/Call with Agent
          <br />
          <div class="control">
            <input type="number" min="1" class="input" v-model="quantity" />
          </div>
          <div class="control">
            <a class="button is-dark" @click="addToCart">Agent Call</a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import { toast } from "bulma-toast";

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
    async getListings() {
      this.$store.commit("setIsLoading", true);

      const country_slug = this.$route.params.country_slug;
      const listings_slug = this.$route.params.listings_slug;

      await axios
        .get(`/api/v1/listings/${country_slug}/${listings_slug}`)
        .then((response) => {
          this.listings = response.data;

          document.title = this.listings.name + " | REA";
        })
        .catch((error) => {
          console.log(error);
        });
      this.$store.commit("setIsLoading", false);
    },
    addToCart() {
      if (isNaN(this.quantity) || this.quantity < 1) {
        this.quantity = 1;
      }

      const item = {
        listings: this.listings,
        quantity: this.quantity,
      };
      this.$store.commit("addToCart", item);

      toast({
        message: "Your schedule with the agent has been added for this listing",
        type: "is-success",
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: "bottom-right",
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
