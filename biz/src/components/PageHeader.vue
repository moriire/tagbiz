<script setup>
import { onMounted, ref } from 'vue'

const props = defineProps({
  mobileNavSection: {
    type: Array,
    required: true,
  },
  contacts: {
    type: Object,
  },
  cartItems: {
    type: Number
  },
})

const isSearchVisible = ref(false)
//const cat = useCategoryStore()
const toggleSearch = () => {
  isSearchVisible.value = !isSearchVisible.value
}
const theme = ref(localStorage.getItem('tagbizTheme') || 'light')
const toggleTheme = () => {
  theme.value = theme.value === 'light' ? 'dark' : 'light'
  localStorage.setItem('tagbizTheme', theme.value)
  document.body.setAttribute('data-bs-theme', theme.value)
}

onMounted(async () => {
  //await cat.getCategories();
  document.body.setAttribute('data-bs-theme', theme.value)
})
</script>
<template>
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
                <i class="fa-solid fa-magnifying-glass fa-2x"></i>
              </a>

              <a
                class="header-action-item header-cart ms-4"
                href="#drawer-cart"
                data-bs-toggle="offcanvas"
              >
                <i class="fa-solid fa-cart-shopping fa-2x"></i>
                <span
                  class="translate-middle badge rounded-pill text-bg-secondary"
                  >{{ props.cartItems.length }}<span class="visually-hidden">Items in Cart</span></span
                >
              </a>
              <button @click="toggleTheme" class="btn header-action-item">
                <div v-if="theme === 'dark'">
                  <i class="fa-regular fa-sun fs-4 fa-2x"></i>
                </div>
                <div v-if="theme === 'light'">
                  <i class="fa-solid fa-circle-half-stroke fs-4 fa-2x"></i>
                </div>
              </button>
              <a
                class="header-action-item header-hamburger ms-4 d-lg-none"
                href="#drawer-menu"
                data-bs-toggle="offcanvas"
              >
                <i class="fa-solid fa-bars fa-2x"></i>
               
              </a>
            </div>
          </div>
        </div>
      </div>

      <div class="search-wrapper d-lg-none" v-if="isSearchVisible">
        <div class="container">
          <form class="search-form d-flex align-items-center">
            <button
              type="submit"
              class="search-submit bg-transparent pl-0 text-start"
            >
              <i class="fa-solid fa-magnifying-glass"></i>
            </button>
            <div class="search-input mr-4">
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
    </div>
    <div class="header-bottom d-lg-block d-none">
      <div class="container">
        <div class="row justify-content-between">
          <div class="col-lg-8">
            <nav class="site-navigation">
              <ul class="main-menu list-unstyled">
                <li
                  class="menu-list-item nav-item"
                  exact
                  v-for="(nav, index) in props.mobileNavSection"
                  v-bind:key="index"
                >
                  <RouterLink :to="nav.route" class="nav-link" exact>{{
                    nav.loc
                  }}</RouterLink>
                </li>
              </ul>
            </nav>
          </div>
          <div class="col-lg-4">
            <nav class="site-navigation">
              <ul class="main-menu list-unstyled float-end mx-0 px-0">
                <li class="menu-list-item nav-item">
                  <a :href="props.contacts.instagram" class="nav-link"
                    ><i class="fa-brands fa-instagram"></i
                  ></a>
                </li>
                <li class="menu-list-item nav-item">
                  <a :href="props.contacts.facebook" class="nav-link"
                    ><i class="fa-brands fa-facebook"></i
                  ></a>
                </li>
                <li class="menu-list-item nav-item">
                  <a :href="props.contacts.whatsapp" class="nav-link"
                    ><i class="fa-brands fa-whatsapp"></i
                  ></a>
                </li>
              </ul>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </header>
</template>