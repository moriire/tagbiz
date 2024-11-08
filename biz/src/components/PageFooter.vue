<script setup>
const props = defineProps({
    owner: {
        type: String,
        required: true
    }
})
</script>
<template>
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
            {{ props.owner }} © <span class="current-year">2024</span>
          </p>
        </div>
      </div>
    </div>
  </footer>
  <!-- footer end -->
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