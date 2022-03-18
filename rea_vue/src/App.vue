<template>
  <div id="wrapper">
    <nav class="navbar is-dark">
      <div class="navbar-logo">
        <router-link to="/" class="navbar-items">
          <strong>REAL ESTATE ANALYTICS</strong>
        </router-link>

        <a
          class="navbar-burger"
          aria-label="menu"
          aria-expanded="false"
          data-target="navbar-menu"
          @click="showMobileMenu = !showMobileMenu"
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div
        class="navbar-menu"
        id="navbar-menu"
        v-bind:class="{ 'is-active': showMobileMenu }"
      >
        <div class="navbar-end">
          <router-link to="/singapore" class="navbar-item"
            >SINGAPORE</router-link
          >
          <router-link to="/hongkong" class="navbar-item"
            >HONG KONG</router-link
          >

          <div class="navbar-item">
            <div class="buttons">
              <router-link to="/login" class="button is-light"
                >Log In</router-link
              >
              <router-link to="/cart" class="button is-success"
                ><span class="icon"><i class="fas fa-shopping-cart"></i></span>
                <span>Cart</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </nav>

    <section class="section">
      <router-view />
    </section>

    <footer class="footer has-text-centered">COPYRIGHT (C) SIREENA KHIN</footer>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showMobileMenu: false,
    };
  },
};
</script>

<style lang="scss">
@import "../node_modules/bulma";
</style>
