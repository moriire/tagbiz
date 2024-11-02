<script setup>

import ProductCard from '../ProductCard.vue';
// Import Swiper Vue.js components
import { Swiper, SwiperSlide } from 'swiper/vue';

// Import Swiper styles
import 'swiper/css';
//import 'swiper/css/pagination';
import 'swiper/css/navigation';

import {
    Autoplay,
    Navigation
    //EffectFade 
} from 'swiper/modules';

defineProps({
    products: {
        type: Array,
        required: true
    },
    title: {
        type: String
    },
    numSlide: {
        type: Number,
        default: 5
    },
    description: {
        type: String
    }

})

const backend = import.meta.env.VITE_BACKEND;
const setImage = (img)=>{
    if (img.startsWith("https://") | img.startsWith("https://")){
        return img
    }
    return `${backend}${img}`
}
const modules = [Autoplay, Navigation]//, EffectFade],
</script>
<template>
     <div class="featured-collection-section mt-100 home-section overflow-hidden">
                <div class="container">
                    <div class="section-header">
                        <h2 class="section-heading">{{ title }}</h2>
                    </div>
    <swiper :slidesPerView="2" :spaceBetween="20" :navigation="true" :breakpoints="{
        '640': {
            slidesPerView: 2,
            spaceBetween: 10,
        },
        '768': {
            slidesPerView: 3,
            spaceBetween: 10,
        },
        '1024': {
            slidesPerView: 4,
            spaceBetween: 20,
        },
    }" :modules="modules" class=".container mySwiper">
            
            <swiper-slide v-for="(product, index) in products" v-bind:key="index">
                <ProductCard
                    :product="product"
                    :image="setImage(product.images[0].img)"
                    @addCart="prod.addToCart(product)" @addWish="wish.addWishlist(product.id)"
                    @click="modalShow(product)" 
                />
            </swiper-slide>
     </swiper>
    </div>
</div>
</template>

<style scoped>
.swiper {
    width: 100%;
    height: 100%;
}

.swiper-slide {
    text-align: center;
    font-size: 18px;
    background: #fff;

    /* Center slide text vertically */
    display: flex;
    justify-content: center;
    align-items: center;
}

.swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
}
</style>