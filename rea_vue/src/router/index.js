import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
import Listings from "../views/Listings.vue";
import Country from "../views/Country.vue";
import Search from "../views/Search.vue";
import Cart from "../views/Cart.vue";
import SignUp from "../views/SignUp.vue";

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },

  {
    path: "/signup",
    name: "SignUp",
    component: SignUp,
  },

  {
    path: "/search",
    name: "Search",
    component: Search,
  },

  {
    path: "/cart",
    name: "Cart",
    component: Cart,
  },

  {
    path: "/:country_slug/:listings_slug",
    name: "Listings",
    component: Listings,
  },

  {
    path: "/:country_slug",
    name: "Country",
    component: Country,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
