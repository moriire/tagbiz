<script setup>
import CartMenu from '@/components/CartMenu.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useProductStore } from '../stores/products'
import { useCategoryStore } from '../stores/categories'
import BreadCrumb from '@/components/BreadCrumb.vue'
import { onBeforeMount, onMounted, ref } from 'vue'
import { useConfigStore } from "@/stores/config";
import { config } from '@vue/test-utils'
const app_conf = useConfigStore()
const prod = useProductStore()
const isSearchVisible = ref(false)
//const cat = useCategoryStore()
const toggleSearch = () => {
  isSearchVisible.value = !isSearchVisible.value
}
const theme = ref(localStorage.getItem("tagbizTheme")|| "light")
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
const toggleTheme = () => {
      theme.value = theme.value === 'light' ? 'dark' : 'light';
      localStorage.setItem("tagbizTheme", theme.value)
      document.body.setAttribute("data-bs-theme", theme.value)
    }
onMounted(async () => {
//await cat.getCategories();
document.body.setAttribute("data-bs-theme", theme.value)
})
</script>

<template>
  <!-- header start -->
  <header class="sticky-header border-btm-black .header-1">
    <div class="header-top border-btm-black">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-3 col-md-4 col-4">
            <div class="header-logo">
              <RouterLink to="/" class="logo-main">
                <h2>Tag<span class="text-warning">Biz</span></h2>
                </RouterLink>
              
            </div>
          </div>
          <div class="col-lg-6 d-lg-block d-none">
            <div class="header-search">
              <form
                role="search"
                class="search-form d-flex justify-content-center"
              >
                <div class="field field-search">
                  <input
                    class="field-input input-reset"
                    type="search"
                    name="q"
                    value=""
                    placeholder="Search here"
                    autocomplete="off"
                  />
                  <button class="search-button btn-reset" type="submit">
                    <i class="fa-solid fa-magnifying-glass"></i>
                  </button>
                </div>
              </form>
            </div>
          </div>
          <div class="col-lg-3 col-md-8 col-8">
            <div
              class="header-action d-flex align-items-center justify-content-end"
            >
              <a
                class="header-action-item header-search d-lg-none"
                type="button"
                @click="toggleSearch()"
              >
              <i class="fa-solid fa-magnifying-glass"></i>
              </a>

              <a
                class="header-action-item header-cart ms-4"
                href="#drawer-cart"
                data-bs-toggle="offcanvas"
              >
                <svg
                  class="icon icon-cart"
                  width="24"
                  height="26"
                  viewBox="0 0 24 26"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M12 0.000183105C9.25391 0.000183105 7 2.25409 7 5.00018V6.00018H2.0625L2 6.93768L1 24.9377L0.9375 26.0002H23.0625L23 24.9377L22 6.93768L21.9375 6.00018H17V5.00018C17 2.25409 14.7461 0.000183105 12 0.000183105ZM12 2.00018C13.6562 2.00018 15 3.34393 15 5.00018V6.00018H9V5.00018C9 3.34393 10.3438 2.00018 12 2.00018ZM3.9375 8.00018H7V11.0002H9V8.00018H15V11.0002H17V8.00018H20.0625L20.9375 24.0002H3.0625L3.9375 8.00018Z"
                    fill="black"
                  />
                </svg>
                <span
                  class="translate-middle badge rounded-pill text-bg-secondary"
                  >{{ prod.cartItems.length
                  }}<span class="visually-hidden">Items in Cart</span></span
                >
              </a>
              <button @click="toggleTheme" class="btn btn-link-dark header-action-item">
                <div v-if="theme==='dark'">
                  <i class="fa-regular fa-sun fs-4" ></i>
                </div>
                <div v-if="theme==='light'">
                  <i class="fa-solid fa-circle-half-stroke fs-4" ></i>
                </div>        
        </button>
              <a
                class="header-action-item header-hamburger ms-4 d-lg-none"
                href="#drawer-menu"
                data-bs-toggle="offcanvas"
              >
                <svg
                  class="icon icon-hamburger"
                  xmlns="http://www.w3.org/2000/svg"
                  width="24"
                  height="24"
                  viewBox="0 0 24 24"
                  fill="none"
                  stroke="#000"
                  stroke-width="2"
                  stroke-linecap="round"
                  stroke-linejoin="round"
                >
                  <line x1="3" y1="12" x2="21" y2="12"></line>
                  <line x1="3" y1="6" x2="21" y2="6"></line>
                  <line x1="3" y1="18" x2="21" y2="18"></line>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="search-wrapper d-lg-none" v-if="isSearchVisible">
        <div class="container">
          <form  class="search-form d-flex align-items-center">
            <button
              type="submit"
              class="search-submit bg-transparent pl-0 text-start"
              
            >
             
              <i class="fa-solid fa-magnifying-glass"></i>
            </button>
            <div class="search-input mr-4" >
              <input
                type="text"
                placeholder="Search your products..."
                autocomplete="off"
              />
            </div>
            <div class="search-close">
              <i class="fa-solid fa-magnifying-glass"></i>            
            </div>
          </form>
        </div>
      </div>
      <div class="header-bottom d-lg-block d-none">
        <div class="container">
          <div class="row justify-content-between">
            <div class="col-lg-8">
              <nav class="site-navigation">
                <ul class="main-menu list-unstyled">
                  <li class="menu-list-item nav-item" exact v-for="(nav, index) in mobileNavSection"
                  v-bind:key="index">
                  <RouterLink :to="nav.route" class="nav-link" >{{ nav.loc }}</RouterLink>
                  </li>
                </ul>
              </nav>
            </div>
            <div class="col-lg-4">
              <nav class="site-navigation">
                <ul class="main-menu list-unstyled float-end mx-0 px-0">
                  <li class="menu-list-item nav-item" >
                  <a :href="app_conf.instagram" class="nav-link" ><i class="fa-brands fa-instagram"></i></a>
                  </li>
                  <li class="menu-list-item nav-item" >
                  <a :href="app_conf.facebook" class="nav-link" ><i class="fa-brands fa-facebook"></i></a>
                  </li>
                  <li class="menu-list-item nav-item" >
                  <a :href="app_conf.whatsapp" class="nav-link" ><i class="fa-brands fa-whatsapp"></i></a>
                  </li>
                 
                </ul>
              </nav>
            </div>
          </div>
        </div>
      </div>
    </div>
  </header>
  <main id="MainContent" class="content-for-layout">
    <RouterView />
  </main>

  <!-- footer start -->
  <footer class="mt-100 overflow-hidden">
    <div class="footer-bottom bg-4">
      <div class="container">
        <div
          class="footer-bottom-inner d-flex flex-wrap justify-content-md-between justify-content-center align-items-center"
        >
          <ul
            class="footer-bottom-menu list-unstyled d-flex flex-wrap align-items-center mb-0"
          >
            <li class="footer-menu-item">
              <a href="/">Privacy policy</a>
            </li>
            <li class="footer-menu-item">
              <a href="/">Terms & Conditions</a>
            </li>
          </ul>
          <p class="copyright footer-text">
            TagBiz Limited © <span class="current-year">2024</span>
          </p>
        </div>
      </div>
    </div>
  </footer>
  <!-- footer end -->
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
            <a :href="`callto:${app_conf.phone}`"> {{ app_conf.phone }} </a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-whatsapp"></i>
            </span>
            <a :href="app_conf.whatsapp"> WhatsApp</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-facebook"></i>
            </span>
            <a :href="app_conf.facebook">Facebook</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-instagram"></i>
            </span>
            <a :href="app_conf.instagram">Instagram</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-solid fa-envelope-open-text"></i>
            </span>
            <a :href="`mailto:${app_conf.email}`">{{ app_conf.email }}</a>
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