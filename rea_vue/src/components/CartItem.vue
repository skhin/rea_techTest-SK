<template>
  <tr>
    <td>
      <router-link :to="item.listings.get_absolute_url">{{
        item.listings.thumbnail
      }}</router-link>
    </td>
    <td>
      <router-link :to="item.listings.get_absolute_url">{{
        item.listings.name
      }}</router-link>
    </td>
    <td>${{ item.listings.price }}</td>
    <td class="has-text-centered">
      {{ item.quantity }}
      <a @click="reduceQty(item)">-</a> |
      <a @click="increaseQty(item)">+</a>
    </td>
    <td class="has-text-centered">7%</td>
    <td>${{ getItemTotal(item).toFixed(2) }}</td>
    <td><button class="delete" @click="removeFromCart(item)"></button></td>
  </tr>
</template>

<script>
export default {
  name: "CartItem",
  props: {
    initialItem: Object,
  },
  data() {
    return {
      item: this.initialItem,
    };
  },
  methods: {
    getItemTotal(item) {
      return item.quantity * item.listings.price * 0.07;
    },
    reduceQty(item) {
      item.quantity -= 1;

      if (item.quantity === 0) {
        this.$emit("removeFromCart", item);
      }
      this.updateCart();
    },
    increaseQty(item) {
      item.quantity += 1;
      this.updateCart();
    },
    updateCart() {
      localStorage.setItem("cart", JSON.stringify(this.$store.state.cart));
    },
    removeFromCart(item) {
      this.$emit("removeFromCart", item);
      this.updateCart();
    },
  },
};
</script>
