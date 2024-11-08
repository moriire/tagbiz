<script setup>
import { useProductStore } from '@/stores/products'
import { useShippingStore } from '@/stores/shipping'
import { computed, onMounted, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import { v4 as uuid4 } from 'uuid'
import axios from 'axios'
const router = useRouter()
let uid = uuid4()
const setImage = (img)=>{
  const backend = import.meta.env.VITE_BACKEND;
    if (img.startsWith("https://") | img.startsWith("https://")){
        return img
    }
    return `${backend}${img}`
}
const prod = useProductStore()
const ship = useShippingStore()
const current = ref(!true)
const paymetApi = import.meta.env.VITE_PAYSTACK_API
const showCart = () =>{
  ship.shippingDetail.transaction.metadata.custom_fields = prod.cartItems
}
const totalAmount = computed(()=> {
  ship.shippingDetail.transaction.amount = (prod.cartSubtotal + ship.shippingCostData.cost - prod.cartTotalDiscount)*100;
  return prod.cartSubtotal + ship.shippingCostData.cost - prod.cartTotalDiscount
}) 
const submitCheckout = async () => {
   try {
    const response = await axios.post(
      'https://api.paystack.co/transaction/initialize',
      ship.shippingDetail.transaction,
      {
        headers: {
          Authorization: `Bearer ${paymetApi}`,
          'Content-Type': 'application/json',
        },
      },
    )
    //console.log(response.data.data.authorization_url)
    location.href = response.data.data.authorization_url
  } catch (err) {
    console.error(err.code)
    console.error(err)
  }
}
onMounted(async () => {
  await ship.getShipping();
  await showCart()
})
</script>
<template>
  <div class="checkout-page mt-100">
    <div class="container">
      <div class="row">
        <div class="col-xl-9 col-lg-8 col-md-12 col-12">
          <div class="header">
            <h2 class=".pb-1">Billing address</h2>
          </div>
          <div class="shipping-address-area">
            <div class=".shipping-address-form-wrapper">
              <form @submit.prevent="submitCheckout">
                <div class="row mb-3">
                  <h2 class="shipping-address-heading pb-1 my-3">Contact</h2>

                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="email">Email address</label>
                    <input
                      required
                      id="email"
                      class="form-control"
                      type="email"
                      v-model="ship.shippingDetail.transaction.email"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="phone">Phone number</label>
                    <input
                      required
                      id="phone"
                      class="form-control"
                      v-model="ship.shippingDetail.transaction.metadata.phone"
                    />
                  </div>
                </div>

                <div class="row my-3">
                  <h2 class="shipping-address-heading pb-1 my-3">Delivery</h2>
                  <div class=".form-check d-grid gap-2">
                    <input
                      type="radio"
                      class="btn-check"
                      id="ship"
                      autocomplete="off"
                      v-model="ship.shippingDetail.transaction.metadata.delivery_mode"
                       value="ship"
                    />
                    <label
                      class="btn btn-secondary d-flex justify-content-between"
                      for="ship"
                    >
                      <span>Ship</span>
                      <span><i class="fa-solid fa-truck-fast"></i></span>
                    </label>
                  </div>
                  <div class=".form-check d-grid gap-2">
                    <input
                      type="radio"
                      class="btn-check"
                       value="pickup"
                      id="pickup"
                      autocomplete="off"
                      v-model="ship.shippingDetail.transaction.metadata.delivery_mode"
                    />
                    <label
                      class="btn btn-secondary d-flex justify-content-between"
                      for="pickup"
                    >
                      <span>Pick Up</span>
                      <span><i class="fa-solid fa-house-circle-check"></i></span>
                    </label>
                  </div>
                  
                </div>

                <div class="row my-3" v-if="ship.shippingDetail.transaction.metadata.delivery_mode === 'ship'">
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="first_name"
                      >First name</label
                    >
                    <input
                      required
                      id="first_name"
                      class="form-control"
                      v-model="ship.shippingDetail.transaction.metadata.first_name"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="last_name">Last name</label>
                    <input
                      required
                      id="last_name"
                      class="form-control"
                      v-model="ship.shippingDetail.transaction.metadata.last_name"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="email">Email address</label>
                    <input
                      required
                      id="email"
                      class="form-control"
                      type="email"
                      v-model="ship.shippingDetail.transaction.metadata.email"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="phone">Phone number</label>
                    <input
                      required
                      id="phone"
                      class="form-control"
                      v-model="ship.shippingDetail.transaction.metadata.phone"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="country">Country</label>
                    <select
                      required
                      id="country"
                      class="form-select"
                      v-model="ship.shippingDetail.transaction.metadata.country"
                    >
                      <option selected value="Nigeria">Nigeria</option>
                    </select>
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="city">City</label>
                    <select
                   
                      required
                      v-if="ship.locations.length>0"
                      class="form-select"
                      v-model="ship.shippingDetail.transaction.metadata.city"
                    >
                      <!--option selected value="">Select City</option-->
                      <option
                      :key="index"
                        :value="loc.region"
                        v-for="(loc, index) in ship.locations"
                      >
                        {{ loc.region }}
                      </option>
                    </select>
                  </div>
                  <div class="col-md-12 col-12">
                    <label class="form-label" for="address">Address</label>
                    <input
                      required
                      id="address"
                      class="form-control"
                      v-model="ship.shippingDetail.transaction.metadata.address"
                      length="20"
                    />
                  </div>

                  <div class="row">
                    <h2 class="shipping-address-heading pb-1 my-3">
                      Shipping Methods
                    </h2>
                    <div
                      class="form-check"
                      v-for="(location, index) in ship.locations"
                    >
                      <input
                        class="form-check-input"
                        type="radio"
                        :value="location.region"
                        :id="'location' + index"
                        v-model="ship.shippingDetail.transaction.metadata.city"
                        :checked="index === 0 ? true : false"
                      />
                      <label class="form-check-label" :for="'location' + index">
                        {{ location.region }}
                      </label>
                      <span class="float-end">&#8358; {{ location.cost }}</span>
                    </div>
                  </div>
                </div>
                 
                  <div class="row my-3" v-if="ship.shippingDetail.transaction.metadata.delivery_mode === 'pickup'">
                    <h2 class="shipping-address-heading pb-1 my-3">
                      Store Location
                    </h2>

                    <div
                      class="border border-primary py-4 px-4 mb-4 d-flex justify-content-between"
              
                    >
                     <p>
                      <strong class="">Put your store address here</strong><br>
                      Adress description</p>
                     <p>Free</p>
                     </div>
                </div>
                <div class="col-md-12 col-12">
                  <div
                    class="d-flex align-items-center justify-content-between flex-wrap"
                  >
                    <RouterLink
                      type="button"
                      to="/cart"
                      class="checkout-page-btn minicart-btn btn-secondary"
                      >BACK TO CART
                    </RouterLink>
                    <input
                      class="checkout-page-btn minicart-btn btn-primary"
                      type="submit"
                      value="CREATE ORDER"
                    />
                   
                    <div class="input-group-text btn-primary" id="basic" v-show="loading" :disbled="disabled">
                  <span class="spinner-border spinner-border-sm" aria-hidden="true">
                  </span>
                </div>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-12 col-12">
          <div class="cart-total-area checkout-summary-area">
            <h3 class="d-none d-lg-block mb-0 text-center text-dark heading_24 mb-4">
              Order summary
            </h3>
            <div
              class="minicart-item d-flex"
              v-for="(cart, index) in prod.cartItems"
              v-bind:key="index"
            >
              <div class="mini-img-wrapper">
                <img class="mini-img" :src="setImage(cart.images[0].img)" alt="img" />
              </div>
              <div class="product-info">
                <h2 class="product-title">
                  <a href="#">{{ cart.name }}</a>
                </h2>
                <p class="product-vendor">
                  &#x20A6;{{ cart.new_price }} x {{ cart.count }}
                </p>
              </div>
            </div>
            <div class="cart-total-box mt-4 bg-transparent p-0">
              <div class="subtotal-item subtotal-box">
                <h4 class="subtotal-title">Subtotals:</h4>
                <p class="subtotal-value">&#x20A6;{{ prod.cartSubtotal }}</p>
              </div>
              <div class="subtotal-item shipping-box">
                <h4 class="subtotal-title">Shipping:</h4>
               
                <p class="subtotal-value" v-if="ship.shippingCostData">
                  &#x20A6;{{ ship.shippingDetail.transaction.metadata.delivery_mode ==='pickup' ? 0 : ship.shippingCostData.cost }}
                </p>
              </div>
              <div class="subtotal-item discount-box">
                <h4 class="subtotal-title">Discount:</h4>
                <p class="subtotal-value">
                  &#x20A6;{{ prod.cartTotalDiscount }}
                </p>
              </div>
              <hr />
              <div class="subtotal-item discount-box">
                <h4 class="subtotal-title">Total:</h4>
                <p class="subtotal-value" v-if="ship.shippingCostData">
                  &#x20A6;{{
                    totalAmount
                  }}
                </p>
              </div>
             
              <!--div class="mt-4 checkout-promo-code">
                    <input class="form-control" class="input-promo-code" type="text" placeholder="Promo code" />
                    <a href="checkout.html" class="btn-apply-code position-relative btn-secondary text-uppercase mt-3">
                      Apply Promo Code
                    </a>
                  </div-->

            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
