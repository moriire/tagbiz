<script setup>
import { ref } from 'vue';
const count = ref(1)
const props = defineProps({
    product: {
        type: Object,
        required: true
    },
    images: {
        type: Array,
        required: true
    },
    count: {
        type: Number,
        default: 1,
    }
})
import { Swiper, SwiperSlide } from 'swiper/vue';
// Import Swiper styles
import 'swiper/css';

import 'swiper/css/free-mode';
import 'swiper/css/navigation';
import 'swiper/css/thumbs';

//import './style.css';

// import required modules
import { FreeMode, Navigation, Thumbs } from 'swiper/modules';
import AtcButton from './buttons/AtcButton.vue';

const thumbsSwiper = ref(null);

const setThumbsSwiper = (swiper) => {
    thumbsSwiper.value = swiper;
};
const modules = [FreeMode, Navigation, Thumbs]
</script>
<template>
    <div class="row">
        <div class="col-lg-6 col-md-12 col-12 " v-if="props.images" style="height: 80vh !important;">
            <swiper :style="{
                '--swiper-navigation-color': '#fff',
                '--swiper-pagination-color': '#fff',
            }" :spaceBetween="10" :navigation="true" :thumbs="{ swiper: thumbsSwiper }"
                :modules="modules" class="mySwiper2">
                <swiper-slide v-for="thumb in images">
                    <img :src="thumb.img" />
                </swiper-slide>
            </swiper>
            <swiper @swiper="setThumbsSwiper" :spaceBetween="10" :slidesPerView="3" :freeMode="true"
                :watchSlidesProgress="true" :modules="modules" class="mySwiper" v-if="product.images===1">
                <swiper-slide v-for="thumb in images">
                    <img :src="thumb.img" />
                </swiper-slide>
            </swiper>
        </div>
        <div class="col-lg-6 col-md-12 col-12" v-if="props.product">
            <div class="product-details ps-lg-4">
                <div class="mb-3">
                    <span class="product-availability">In Stock</span>
                </div>
                <h2 class="product-title mb-3">{{ props.product.name }}</h2>
                <div class="product-price-wrapper mb-4">
                    <span class="product-price regular-price">&#x20A6; {{ props.product.new_price }}</span>
                    <del class="product-price compare-price ms-2">&#x20A6; {{ props.product.price }}</del>
                </div>
               
                <div>
                    <strong class="label">Description:</strong><br>
                    <p>
                        {{ props.product.description }}
                    </p>
                </div>
                <div class="misc d-flex align-items-end justify-content-between mt-4">
                    <div class="quantity d-flex align-items-center justify-content-between">
                        <button class="qty-btn dec-qty" @click="count-=1">
                            <i class="fa-solid fa-minus"></i>
                        </button>
                        <input class="qty-input" type="number" name="qty" v-model="count" min="0">
                        <button class="qty-btn inc-qty" @click="count+=1">
                            <i class="fa-solid fa-plus"></i>
                        </button>
                    </div>
                  </div>

                <div class="product-form-buttons d-flex align-items-center justify-content-between mt-3">
                    <AtcButton :product_obj="product" class="me-2 .position-relative btn-atc btn-add-to-cart loader" />
                    <button type="submit" class="me-2 .position-relative btn-atc btn-buyit-now">BUY IT
                        NOW</button>
                   

                </div>
               
            </div>
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

.swiper {
    width: 100%;
    height: 300px;
    margin-left: auto;
    margin-right: auto;
}

.swiper-slide {
    background-size: cover;
    background-position: center;
}

.mySwiper2 {
    height: 80% !important;
    width: 100%;
}

.mySwiper {
    height: 20% !important;
    box-sizing: border-box;
    padding: 10px 0;
}

.mySwiper .swiper-slide {
    width: 25%;
    height: 100%;
    opacity: 0.4;
}

.mySwiper .swiper-slide-thumb-active {
    opacity: 1;
}

.swiper-slide img {
    display: block;
    width: 100%;
    height: 100%;
    object-fit: cover;
}

;
</style>