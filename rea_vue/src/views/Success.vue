<template>
  <div class="page-success">
    <div class="columns is-multiline">
      <div class="column is-12">
        <h1 class="title">Thank you</h1>

        <p>
          An agent will get back to you within the next 1-2 business working
          days
        </p>
      </div>
      <router-link to="/" class="button is-dark">
        <button class="button is-dark">Back to Home Page</button>
      </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Success",
  mounted() {
    document.title = "Success | REA";
  },
};
</script>
