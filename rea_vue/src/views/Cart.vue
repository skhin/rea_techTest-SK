<template>
  <div class="page-cart">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">CART</h1>
      </div>

      <div class="column is-12 box">
        <table class="table is-fullwidth" v-if="cartTotalLength">
          <thead>
            <tr>
              <th></th>
              <th>Listing</th>
              <th>Price</th>
              <th>Quantity</th>
              <th>Tax(GST)</th>
              <th>Total</th>
              <th></th>
            </tr>
          </thead>

          <tbody>
            <CartItem
              v-for="item in cart.items"
              v-bind:key="item.listings.id"
              v-bind:initialItem="item"
              v-on:removeFromCart="removeFromCart"
            />
          </tbody>
        </table>
        <p v-else>You don't have any listings in your cart...</p>
      </div>

      <div class="column is-12 box">
        <h2 class="subtitle">Summary</h2>

        <strong>${{ cartTotalPrice.toFixed(2) }}</strong
        >, {{ cartTotalLength }} Listings

        <hr />

        <router-link to="/cart/checkout" class="button is-dark"
          >Proceed to checkout</router-link
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import CartItem from "../components/CartItem";

export default {
  name: "Cart",
  components: {
    CartItem,
  },
  data() {
    return {
      cart: {
        items: [],
      },
    };
  },
  mounted() {
    this.cart = this.$store.state.cart;
  },
  methods: {
    removeFromCart(item) {
      this.cart.items = this.cart.items.filter(
        (i) => i.listings.id !== item.listings.id
      );
    },
  },
  computed: {
    cartTotalLength() {
      return this.cart.items.reduce((acc, currentValue) => {
        return (acc += currentValue.quantity);
      }, 0);
    },
    cartTotalPrice() {
      return this.cart.items.reduce((acc, currentValue) => {
        return (acc +=
          currentValue.listings.price * currentValue.quantity * 0.07);
      }, 0);
    },
  },
};
</script>
