<script setup>
defineProps({
  products: {
    type: Array,
    required: true,
  },
  show: {
    type: Boolean,
    default: false,
  },
})
import QuickView from './QuickView.vue'
import ProductCard from './ProductCard.vue'
import { useProductStore } from '@/stores/products'
import { ref } from 'vue'
import AtcButton from './buttons/AtcButton.vue'
const prod = useProductStore()
const item = ref({})
const modalShow = async p => {
  item.value = p
}
</script>

<template>
  <div class="container">
    <div class="row justify-content-center">
      <div
        class="col-lg-3 col-md-4 col-6"
        data-aos="fade-up"
        :data-aos-duration="200 * (index + 1)"
        v-for="(product, index) in products"
        v-bind:key="product.slug"
      >
        <!--button @click="prod.addToCart(product)">Add({{ prod.cartItems.length }})</button-->
        <ProductCard
          :product="product"
          v-if="product.images.length"
          :image="product.images[0].img"
          @click="modalShow(product)"
        />
      </div>

    </div>
  </div>
  <!-- product quickview start -->
  <QuickView :item="item" />
  <!-- product quickview end -->
</template>
