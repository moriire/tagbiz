<script setup>
import CartMenu from '@/components/CartMenu.vue'
import PageFooter from '@/components/PageFooter.vue'
import PageHeader from '@/components/PageHeader.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useProductStore } from '../stores/products'
import { useCategoryStore } from '../stores/categories'
import { onBeforeMount, onMounted, ref } from 'vue'
import { useConfigStore } from "@/stores/config";
import { config } from '@vue/test-utils'
const app_conf = useConfigStore()
const prod = useProductStore()

const navSection = [
  { loc: 'Home', route: '/', icon: 'las la-home' },
  {
    loc: 'Shop',
    route: '/shop',
    icon: 'las la-gifts',
    submenu: [
      { loc: 'All Products', route: '/shop' },
      { loc: 'View Cart', route: '/cart', icon: 'las la-cart-plus' },
      { loc: 'Checkout', route: '/checkout', icon: 'las la-cash-register' },
    ],
  },
  { loc: 'About Us', route: '/contact', icon: 'las la-book' },
  { loc: 'Contact Us', route: '/contact', icon: 'las la-pen' },
]
const mobileNavSection = [
  { loc: 'Home', route: '/', icon: 'las la-home' },
  {
    loc: 'Shop',
    route: '/shop',
    icon: 'las la-gifts',
  },
  { loc: 'Cart', route: '/cart', icon: 'las la-cart-plus' },
  { loc: 'Checkout', route: '/checkout', icon: 'las la-cash-register' },
  { loc: 'About Us', route: '/contact', icon: 'las la-book' },
  { loc: 'Contact Us', route: '/contact', icon: 'las la-pen' },
]
</script>

<template>
  <PageHeader :mobileNavSection="mobileNavSection" :contacts="app_conf.config" :cartItems="prod.cartItems"/>
  <main id="MainContent" class="content-for-layout">
    <RouterView />
  </main>
<PageFooter owner="tagbiz" />
 
  <!-- scrollup start -->
  <button id="scrollup">
    <i class="fa-solid fa-caret-up"></i>
  </button>
  <!-- scrollup end -->
  <!-- drawer menu start -->
  <div
    class="offcanvas offcanvas-start d-flex offcanvas-sm"
    tabindex="-1"
    id="drawer-menu"
  >
    <div class="offcanvas-wrapper">
      <div class="offcanvas-header border-btm-black">
        <h5 class="drawer-heading">Tag<span class="text-warning">Biz</span></h5>
        <button
          type="button"
          class="btn-close text-reset"
          data-bs-dismiss="offcanvas"
          aria-label="Close"
        ></button>
      </div>
      <div
        class="offcanvas-body p-0 d-flex flex-column justify-content-between"
      >
        <nav class="site-navigation">
          <ul class="main-menu list-unstyled">
            <li
              class="menu-list-item nav-item"
              v-for="(nav, index) in mobileNavSection"
              v-bind:key="index"
            >
              <RouterLink exact class="nav-link" :to="nav.route">{{
                nav.loc
              }}</RouterLink>
            </li>
          </ul>
        </nav>
        <ul class="utility-menu list-unstyled">
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-solid fa-phone"></i>
            </span>
            <a :href="`callto:${app_conf.phone}`"> {{ app_conf.config.phone }} </a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-whatsapp"></i>
            </span>
            <a :href="app_conf.config.whatsapp"> WhatsApp</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-facebook"></i>
            </span>
            <a :href="app_conf.config.facebook">Facebook</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-instagram"></i>
            </span>
            <a :href="app_conf.config.instagram">Instagram</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-solid fa-envelope-open-text"></i>
            </span>
            <a :href="`mailto:${app_conf.config.email}`">{{ app_conf.config.email }}</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- drawer menu end -->

  <CartMenu :cartItems="prod.cartItems" />
</template>
<style scoped>
.offcanvas-xs {
    --bs-offcanvas-width: 65vw !important;
}
.offcanvas-sm {
    --bs-offcanvas-width: 65vw !important;
}
</style>