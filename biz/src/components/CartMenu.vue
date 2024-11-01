<script setup>
import { RouterLink, useRouter } from 'vue-router';
import CartItem from './CartItem.vue';
import { useProductStore } from '@/stores/products';
defineProps({
  cartItems: {
    type: Array,
    required: true
  }
});
const prod = useProductStore()
const router = useRouter()
const goTo = (loc)=> router.push(loc)
</script>

<template>
     <!-- drawer cart start -->
     <div class="offcanvas offcanvas-end" tabindex="-1" id="drawer-cart">
            <div class="offcanvas-header border-btm-black">
                <h5 class="cart-drawer-heading text_16">Your Cart ({{ cartItems.length }})</h5>
                <button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas"
                    aria-label="Close"></button>
            </div>
            <div class="offcanvas-body p-0">
                <div class="cart-content-area d-flex justify-content-between flex-column">
                  <div class="m-2 text-center" v-if="cartItems.length === 0">
                    <h3>
                      No item in cart. Go to <RouterLink to="/shop">Shop</RouterLink> to add product
                    </h3>
                  </div>  
                  <div class="minicart-loop custom-scrollbar" v-else> 
                      <template v-for="(cart, index) in cartItems" v-bind:key="index">
                         <CartItem 
                         :item = "cart"
                          @removeCart="prod.deleteCartLocal(cart)" 
                        />
                      </template>
                    </div>
                    <div class="minicart-footer">
                        <div class="minicart-calc-area">
                            <div class="minicart-calc d-flex align-items-center justify-content-between">
                                <span class="cart-subtotal mb-0">Subtotal</span>
                                <span class="cart-subprice">&#x20A6;{{ prod.cartSubtotal }}</span>
                            </div>
                            <p class="cart-taxes text-center my-4">Taxes and shipping will be calculated at checkout.
                            </p>
                        </div>
                        <div class="minicart-btn-area d-flex align-items-center justify-content-between">
                            <button @click="goTo('/cart')" class="minicart-btn btn-secondary" :disabled="cartItems.length === 0" >View Cart</button>
                            <button @click="goTo('/checkout')" class="minicart-btn btn-primary" :disabled="cartItems.length === 0" >Checkout</button>
                        </div>
                    </div>
                </div>
                <div class="cart-empty-area text-center py-5 d-none">
                    <div class="cart-empty-icon pb-4">
                        <svg xmlns="http://www.w3.org/2000/svg" width="70" height="70" viewBox="0 0 24 24" fill="none"
                            stroke="currentColor" stroke-width="1" stroke-linecap="round" stroke-linejoin="round"
                            >
                            <circle cx="12" cy="12" r="10"></circle>
                            <path d="M16 16s-1.5-2-4-2-4 2-4 2"></path>
                            <line x1="9" y1="9" x2="9.01" y2="9"></line>
                            <line x1="15" y1="9" x2="15.01" y2="9"></line>
                        </svg>
                    </div>
                    <p class="cart-empty">You have no items in your cart</p>
                </div>
            </div>
        </div>
        <!-- drawer cart end --> 
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
