<script setup>
import { onMounted } from 'vue'
import CartMenu from '@/components/CartMenu.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useProductStore } from '../stores/products'
import { useCategoryStore } from '../stores/categories'
import BreadCrumb from '@/components/BreadCrumb.vue'
const prod = useProductStore()
//const cat = useCategoryStore()
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
//onMounted(async () => {
//await cat.getCategories();
//})
</script>

<template>
  <!-- header start -->
  <header class="sticky-header border-btm-black header-1">
    <div class="header-bottom">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-lg-2 col-md-4 col-4">
            <div class="header-logo">
              <RouterLink to="/" class="logo-main">
                <h2>Tag<span class="text-warning">Biz</span></h2>
                <!--img src="/src/assets/img/logo.png" loading="lazy" alt="tagbiz"-->
              </RouterLink>
            </div>
          </div>
          <div class="col-lg-8 d-lg-block d-none">
            <nav class="site-navigation">
              <ul class="main-menu list-unstyled justify-content-center">
                <template v-for="(nav, index) in navSection" v-bind:key="index">
                  <li
                    class="menu-list-item nav-item has-dropdown"
                    v-if="nav.submenu"
                  >
                    <div class="mega-menu-header">
                      <a type="button" class="nav-link">
                        {{ nav.loc }}
                      </a>
                      <span class="open-submenu">
                        <svg
                          class="icon icon-dropdown"
                          xmlns="http://www.w3.org/2000/svg"
                          width="24"
                          height="24"
                          viewBox="0 0 24 24"
                          fill="none"
                          stroke="currentColor"
                          stroke-width="2"
                          stroke-linecap="round"
                          stroke-linejoin="round"
                        >
                          <polyline points="6 9 12 15 18 9"></polyline>
                        </svg>
                      </span>
                    </div>
                    <div class="submenu-transform submenu-transform-desktop">
                      <ul class="submenu list-unstyled">
                        <li
                          class="menu-list-item nav-item-sub"
                          v-for="(sm, ind) in nav.submenu"
                          v-bind:key="ind"
                        >
                          <RouterLink
                            class="nav-link-sub nav-text-sub"
                            :to="sm.route"
                            >{{ sm.loc }}</RouterLink
                          >
                        </li>
                      </ul>
                    </div>
                  </li>

                  <li class="menu-list-item nav-item" v-else>
                    <RouterLink :to="nav.route" class="nav-link" exact>
                      <i :class="nav.icon"></i> <span>{{ nav.loc }}</span>
                    </RouterLink>
                  </li>
                </template>

                <li class="menu-list-item nav-item has-dropdown">
                  <div class="submenu-transform submenu-transform-desktop">
                    <ul class="submenu list-unstyled">
                      <li class="menu-list-item nav-item-sub">
                        <RouterLink class="nav-link-sub nav-text-sub" to="/faq"
                          >FAQ</RouterLink
                        >
                      </li>
                      <li class="menu-list-item nav-item-sub">
                        <RouterLink
                          class="nav-link-sub nav-text-sub"
                          to="/contact"
                          >Contact
                        </RouterLink>
                      </li>
                    </ul>
                  </div>
                </li>
              </ul>
            </nav>
          </div>
          <div class="col-lg-2 col-md-8 col-8">
            <div
              class="header-action d-flex align-items-center justify-content-end"
            >
              <a class="header-action-item header-search" type="button">
                <svg
                  class="icon icon-search"
                  width="20"
                  height="20"
                  viewBox="0 0 20 20"
                  fill="none"
                  xmlns="http://www.w3.org/2000/svg"
                >
                  <path
                    d="M7.75 0.250183C11.8838 0.250183 15.25 3.61639 15.25 7.75018C15.25 9.54608 14.6201 11.1926 13.5625 12.4846L19.5391 18.4611L18.4609 19.5392L12.4844 13.5627C11.1924 14.6203 9.5459 15.2502 7.75 15.2502C3.61621 15.2502 0.25 11.884 0.25 7.75018C0.25 3.61639 3.61621 0.250183 7.75 0.250183ZM7.75 1.75018C4.42773 1.75018 1.75 4.42792 1.75 7.75018C1.75 11.0724 4.42773 13.7502 7.75 13.7502C11.0723 13.7502 13.75 11.0724 13.75 7.75018C13.75 4.42792 11.0723 1.75018 7.75 1.75018Z"
                    fill="black"
                  />
                </svg>
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
      <div class="search-wrapper">
        <div class="container">
          <form action="#" class="search-form d-flex align-items-center">
            <button
              type="submit"
              class="search-submit bg-transparent pl-0 text-start"
            >
              <svg
                class="icon icon-search"
                width="20"
                height="20"
                viewBox="0 0 20 20"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <path
                  d="M7.75 0.250183C11.8838 0.250183 15.25 3.61639 15.25 7.75018C15.25 9.54608 14.6201 11.1926 13.5625 12.4846L19.5391 18.4611L18.4609 19.5392L12.4844 13.5627C11.1924 14.6203 9.5459 15.2502 7.75 15.2502C3.61621 15.2502 0.25 11.884 0.25 7.75018C0.25 3.61639 3.61621 0.250183 7.75 0.250183ZM7.75 1.75018C4.42773 1.75018 1.75 4.42792 1.75 7.75018C1.75 11.0724 4.42773 13.7502 7.75 13.7502C11.0723 13.7502 13.75 11.0724 13.75 7.75018C13.75 4.42792 11.0723 1.75018 7.75 1.75018Z"
                  fill="black"
                />
              </svg>
            </button>
            <div class="search-input mr-4">
              <input
                type="text"
                placeholder="Search your products..."
                autocomplete="off"
              />
            </div>
            <div class="search-close">
              <svg
                xmlns="http://www.w3.org/2000/svg"
                width="24"
                height="24"
                viewBox="0 0 24 24"
                fill="none"
                stroke="currentColor"
                stroke-width="2"
                stroke-linecap="round"
                stroke-linejoin="round"
                class="icon icon-close"
              >
                <line x1="18" y1="6" x2="6" y2="18"></line>
                <line x1="6" y1="6" x2="18" y2="18"></line>
              </svg>
            </div>
          </form>
        </div>
      </div>
    </div>
  </header>
  <bread-crumb></bread-crumb>
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
              <a href="about-us.html">Privacy policy</a>
            </li>
            <li class="footer-menu-item">
              <a href="about-us.html">Terms & Conditions</a>
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
    <svg
      xmlns="http://www.w3.org/2000/svg"
      width="24"
      height="24"
      viewBox="0 0 24 24"
      fill="none"
      stroke="#fff"
      stroke-width="2"
      stroke-linecap="round"
      stroke-linejoin="round"
    >
      <polyline points="18 15 12 9 6 15"></polyline>
    </svg>
  </button>
  <!-- scrollup end -->
  <!-- drawer menu start -->
  <div
    class="offcanvas offcanvas-start d-flex d-lg-none"
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
            <a href="callto:+234902334664"> +234(90)2 3394 664 </a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-brands fa-whatsapp"></i>
            </span>
            <a href="https://wa.me/+234902334664"> WhatsApp<</a>
          </li>
          <li class="utilty-menu-item">
            <span class="utilty-icon-wrapper">
              <i class="fa-solid fa-envelope-open-text"></i>
            </span>
            <a href="mailto:agesxpat@gmail.com">agesxpat@gmail.com<</a>
          </li>
        </ul>
      </div>
    </div>
  </div>
  <!-- drawer menu end -->

  <CartMenu :cartItems="prod.cartItems" />
</template>
