<script setup>
import { useProductStore } from '@/stores/products';
import { onMounted, watchEffect } from 'vue';
import { useRoute } from 'vue-router';
import ProductSingle from '@/components/ProductSingle.vue';
//import DiscountedSlide from '@/components/home/DiscountedSlide.vue';
const prod = useProductStore();
const route = useRoute()
watchEffect(
    async () => await prod.singeProduct(route.params.product)
)
onMounted(async () => await prod.singeProduct(route.params.product))
</script>
<template>
    <div class="product-page mt-100">
        <div class="container">
            <div class="row">
                <!-- product quickview start -->
                <ProductSingle :images="prod.product.images" :product="prod.product" @addCart="prod.addToCartLocal(prod.product)"
                    @addWish="prod.addToCartLocal(prod.product.id)" />
                <!-- product quickview end -->
            </div>
        </div>
    </div>
</template>