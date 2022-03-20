<template>
  <div class="page-checkout">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Checkout</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth">
          <thead>
            <tr>
              <th>Listing</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Total</th>
            </tr>
          </thead>

          <tbody>
            <tr v-for="item in cart.items" v-bind:key="item.listings.id">
              <td>{{ item.listings.name }}</td>
              <td>${{ item.listings.price }}</td>
              <td>{{ item.quantity }}</td>
              <td>${{ getItemTotal(item).toFixed(2) }}</td>
            </tr>
          </tbody>

          <tfoot>
            <tr>
              <td colspan="2"><strong>Total</strong></td>
              <td>{{ cartTotalLength }}</td>
              <td>
                <strong>${{ cartTotalPrice.toFixed(2) }}</strong>
              </td>
            </tr>
          </tfoot>
        </table>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Order details</h2>

        <p class="has-text-grey mb-4">* All fields are required</p>

        <div class="columns is-multiline">
          <div class="column is-6">
            <div class="field">
              <label>First name*</label>
              <div class="control">
                <input type="text" class="input" v-model="first_name" />
              </div>
            </div>

            <div class="field">
              <label>Last name*</label>
              <div class="control">
                <input type="text" class="input" v-model="last_name" />
              </div>
            </div>

            <div class="field">
              <label>E-mail*</label>
              <div class="control">
                <input type="email" class="input" v-model="email" />
              </div>
            </div>

            <div class="field">
              <label>Phone*</label>
              <div class="control">
                <input type="text" class="input" v-model="phone" />
              </div>
            </div>
          </div>

          <div class="column is-6">
            <div class="field">
              <label>Address*</label>
              <div class="control">
                <input type="text" class="input" v-model="address" />
              </div>
            </div>

            <div class="field">
              <label>Zip code*</label>
              <div class="control">
                <input type="text" class="input" v-model="zipcode" />
              </div>
            </div>

            <div class="field">
              <label>Place*</label>
              <div class="control">
                <input type="text" class="input" v-model="place" />
              </div>
            </div>
          </div>
        </div>

        <div class="notification is-danger mt-4" v-if="errors.length">
          <p v-for="error in errors" v-bind:key="error">{{ error }}</p>
        </div>

        <hr />

        <div id="card-element" class="mb-5"></div>

        <template v-if="cartTotalLength">
          <hr />
          <router-link to="/cart/success" class="button is-dark">
            <button class="button is-dark">Pay with Stripe</button>
          </router-link>
        </template>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Checkout",
  data() {
    return {
      cart: {
        items: [],
      },
      stripe: {},
      card: {},
      first_name: "",
      last_name: "",
      email: "",
      phone: "",
      address: "",
      zipcode: "",
      place: "",
      errors: [],
    };
  },
  mounted() {
    document.title = "Checkout | REA";

    this.cart = this.$store.state.cart;
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.listings.price;
    },
  },
  computed: {
    cartTotalPrice() {
      return this.cart.items.reduce((acc, currentValue) => {
        return (acc += currentValue.listings.price * currentValue.quantity);
      }, 0);
    },
    cartTotalLength() {
      return this.cart.items.reduce((acc, currentValue) => {
        return (acc += currentValue.quantity);
      }, 0);
    },
  },
};
</script>
