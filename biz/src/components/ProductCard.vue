<script setup>
import { RouterLink } from 'vue-router';
import AtcButton from "./buttons/AtcButton.vue"
//import AtwButton from './buttons/AtwButton.vue';
//import RfcButton from './buttons/RfcButton.vue';

const prop = defineProps({
  product: {
    type: Object,
    required: true
  },
  delObjectId: {
    type: Number
  },
  cta: {
    type: String,
    default: "add"
  },
  image: {
    type: String,
    required: true
  },
})
</script>
<template>
  <div class="product-card" v-if="prop.product">
      <div class="product-card-img">
        <RouterLink class="hover-switch" :to="{name: 'product-detail', params:{product: prop.product.id } }">
          <div class="product-badge">
            <span class="badge-label badge-percentage rounded">{{ prop.product.discount > 0 ? `-${prop.product.discount}%` : prop.product.condition }}</span>
          </div>
          <img class="primary-img" :src="prop.image" :alt="prop.product.name">
          </RouterLink>

        <div class="product-card-action product-card-action-2">
          <a href="#quickview-modal" class="quickview-btn btn-primary" data-bs-toggle="modal">QUICKVIEW</a>
          
              <AtcButton :product_obj="prop.product" />
        </div>
        <!--AtwButton :product_id="prop.product.id" v-if="cta == 'add'" /-->
        <!--RfcButton :product_id="prop.delObjectId" v-if="cta === 'remove'" /-->
      </div>
      <div class="product-card-details text-center">
        
        <h3 class="product-card-title">
          <RouterLink  :to="{name: 'product-detail', params:{product: prop.product.id } }">
            {{ prop.product.name }}
         </RouterLink>
         
        </h3>
        <div class="product-card-product.price">
          <span class="card-price-regular">&#x20A6;{{ prop.product.price }}</span>
          <span class="card-price-compare text-decoration-line-through" v-if="prop.product.discount>0">&#x20A6;{{ product.new_price }}</span>
        </div>
      </div>

    </div>
</template>

<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

@media (min-width: 1024px) {

  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
