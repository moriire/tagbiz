<script setup>
import { onMounted } from 'vue'
//import CartMenu from '@/components/CartMenu.vue'
import { RouterLink, RouterView } from 'vue-router'
import { useProductStore } from '@/stores/products'
import { useCategoryStore } from './stores/categories'

const prod = useProductStore()
const cat = useCategoryStore()
onMounted(async () => {
  await cat.getCategories();
  
})
</script>

<template>
  <RouterView />
</template>
<style>
:root {
  --primary-color: #00234d;
  --secondary-color: #f76b6a;

  --btn-primary-border-radius: 0.25rem;
  --btn-primary-color: #fff;
  --btn-primary-background-color: #00234d;
  --btn-primary-border-color: #00234d;
  --btn-primary-hover-color: #fff;
  --btn-primary-background-hover-color: #00234d;
  --btn-primary-border-hover-color: #00234d;
  --btn-primary-font-weight: 500;

  --btn-secondary-border-radius: 0.25rem;
  --btn-secondary-color: #00234d;
  --btn-secondary-background-color: transparent;
  --btn-secondary-border-color: #00234d;
  --btn-secondary-hover-color: #fff;
  --btn-secondary-background-hover-color: #00234d;
  --btn-secondary-border-hover-color: #00234d;
  --btn-secondary-font-weight: 500;

  --heading-color: #000;
  --heading-font-family: 'Poppins', sans-serif;
  --heading-font-weight: 700;

  --title-color: #000;
  --title-font-family: 'Poppins', sans-serif;
  --title-font-weight: 400;

  --body-color: #000;
  --body-background-color: #fff;
  --body-font-family: 'Poppins', sans-serif;
  --body-font-size: 14px;
  --body-font-weight: 400;

  --section-heading-color: #000;
  --section-heading-font-family: 'Poppins', sans-serif;
  --section-heading-font-size: 48px;
  --section-heading-font-weight: 600;

  --section-subheading-color: #000;
  --section-subheading-font-family: 'Poppins', sans-serif;
  --section-subheading-font-size: 16px;
  --section-subheading-font-weight: 400;
}
</style>
