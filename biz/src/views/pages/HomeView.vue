<script setup>
import { onMounted, ref } from 'vue';
import { RouterLink, useRoute } from 'vue-router';
import { useCategoryStore } from '@/stores/categories';
import HomeSkeleton from "@/components/home/HomeSkeleton.vue"
//import HeroSlide from "@/components/home/HeroSlide.vue"
import ProductPage from "@/components/ProductPage.vue"
import { useProductStore } from '@/stores/products';
import CategoriesSlide from "@/components/home/CategoriesSlide.vue"
//import VendorSlide from '@/components/VendorSlide.vue';
import DiscountedSlide from "@/components/home/DiscountedSlide.vue"
import { useHomeStore } from '@/stores/home';
//import GridedProducts from '@/components/GridedProducts.vue';
import { useConfigStore } from "@/stores/config";
const app_conf = useConfigStore()
const cat = useCategoryStore()
const prod = useProductStore()
const home = useHomeStore()
const loading = ref(false)
onMounted(async () => {
    loading.value = true;
    await home.getLatest();
        await home.getPromoted();
        await home.getDiscounted();
        await prod.getProducts();
        loading.value=false
})
</script>
<template>
    <HomeSkeleton>
        <template v-slot:categories>
            <!-- promotinal product start -->
            <div class="promotinal-product-section overlay-tools overflow-hidden" :style="`background-image: url(${app_conf.config.hero})`" style="background-color:#000;  background-repeat: no-repeat; background-position: center; background-size: cover; color: white">
                <div class="container-fluid">
                    <div class="row">
                        <div class="col-lg-4 col-12 d-flex align-items-center">
                            <div class="promotinal-product-content" data-aos="fade-up" data-aos-duration="700">
                                <!--p class="heading_18 primary-color mb-3">Navigate our various product categories</p-->
                                <h2 class="heading_34 text-white my-4">{{ app_conf.config.subtitle }}</h2>
                                <p class="text_16 text-white my-4">
                                    {{ app_conf.config.description }}
                                </p>
                                <div class=".view-all my-4">
                                    <RouterLink class="btn-primary" to="/shop">START SHOPPING</RouterLink>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-8 col-12 align-self-center">
                            <CategoriesSlide :items="cat.categories" v-if="cat.categories.length"/>

                        </div>
                    </div>
                </div>
            </div>
            <!-- promotinal product end -->
        </template>
        <template v-slot:latest>
            <!-- collection start -->
            <div class="featured-collection mt-100 overflow-hidden">
                <div class="collection-tab-inner">
                    <div class="container">
                        <div class="section-header text-center">
                            <h2 class="section-heading">Latest Products</h2>
                        </div>
                        <div class="row">
                            <ProductPage :products="home.latests" v-if="home.latests.length" />
                          
                            <template v-else>
                                <div class="vh-100 d-flex justify-content-center align-items-center">
                                    <h2>No Products Uploaded yet</h2>
                                </div>
                            </template>
                        </div>
                        <div class="view-all text-center" data-aos="fade-up" data-aos-duration="700">
                            <RouterLink class="btn-primary" to="/shop">VIEW ALL</RouterLink>
                        </div>
                    </div>
                </div>
            </div>
            <!-- collection end -->
        </template>
        <template v-slot:discounted>
           
                    <DiscountedSlide :products="home.discounteds" :numSlide="4" v-if="home.discounteds.length" />
        </template>
    </HomeSkeleton>
</template>