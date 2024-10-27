<script setup>
import { useProductStore } from '@/stores/products'
import { useShippingStore } from '@/stores/shipping'
import { onMounted, ref } from 'vue'
import { RouterLink } from 'vue-router'
import { v4 as uuid4 } from 'uuid'
import axios from 'axios'

let uid = uuid4()
const prod = useProductStore()
const ship = useShippingStore()
const current = ref(!true)
const deliv = ref("ship")
const deliveryTypes = {
  ship: "Ship",
  pickup: "pick up in store"
}
const form = ref({
  tx_ref: uid,
  amount: prod.totalPrice,
  paymentMethod: 'credit_card',
  redirect_url: '',
  max_retry_attempt: 5,
  customer: {
    email: '',
    name: '',
    phonenumber: '',
  },
  customizations: {
    title: 'Welcome to TagBiz',
    description: '',
  },
})

const submitCheckout = async () => {
  try {
    const response = await axios.post(
      'https://api.flutterwave.com/v3/payments',
      form.value,
      {
        headers: {
          Authorization: `Bearer ${process.env.FLW_SECRET_KEY}`,
          'Content-Type': 'application/json',
        },
      },
    )
  } catch (err) {
    console.error(err.code)
    console.error(err)
  }
}
onMounted(async () => {
  await ship.getShipping()
  //await ship.getShippingCost()
})
</script>

<template>
  <div class="checkout-page mt-100">
    <div class="container">
      <div class="row">
        <div class="col-xl-9 col-lg-8 col-md-12 col-12">
          <div class="header">
            <h2 class=".pb-1">Billing address</h2>
          </div>{{ deliv }}
          <div class="shipping-address-area">
            <div class=".shipping-address-form-wrapper">
              <form @submit.prevent="prod.addForShipping">
                <div class="row mb-3">
                  <h2 class="shipping-address-heading pb-1 my-3">Contact</h2>

                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="email">Email address</label>
                    <input
                      required
                      id="email"
                      class="form-control"
                      type="email"
                      v-model="ship.shippingDetail.email"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="phone">Phone number</label>
                    <input
                      required
                      id="phone"
                      class="form-control"
                      v-model="ship.shippingDetail.phone"
                    />
                  </div>
                </div>
     
                <div class="row my-3">
                  <h2 class="shipping-address-heading pb-1 my-3">Delivery</h2>

                 <div
                    class=".form-check" >
                    
                    <label class=" d-flex justify-content-between align-items-center form-check-label " for="ship" style="border:1px solid; padding: 2px 5px !important;">
                     <span>
                      <input
                    required
                      class=".form-check-input my-3 .d-block me-2"
                      type="radio"
                      value="ship"
                      id="ship"
                      v-model="deliv"
                      
                    /> Ship </span> <span class="float-end "><i class="fa-solid fa-truck-fast"></i></span>
                  
                    </label>
                    </div>
                  <div class=".form-check ">
                    <label class=" d-flex justify-content-between align-items-center .form-check-label" for="ship" style="border:1px solid; padding: 2px 5px !important;">
                      <span>
                    <input
                      class=".form-check-input my-3 .d-block me-2"
                      reuired
                      type="radio"
                      value="pickup"
                      id="pickup"
                      v-model="deliv"
                    />Pick Up</span>
                    <span class="float-end "><i class="fa-solid fa-house-circle-check"></i></span>
                 
                    </label>
                   </div>
                </div>

                <div class="row my-3" v-if="deliv==='ship'">
                  
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="first_name"
                      >First name</label
                    >
                    <input
                      required
                      id="first_name"
                      class="form-control"
                      v-model="ship.shippingDetail.first_name"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="last_name">Last name</label>
                    <input
                      required
                      id="last_name"
                      class="form-control"
                      v-model="ship.shippingDetail.last_name"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="email">Email address</label>
                    <input
                      required
                      id="email"
                      class="form-control"
                      type="email"
                      v-model="ship.shippingDetail.email"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="phone">Phone number</label>
                    <input
                      required
                      id="phone"
                      class="form-control"
                      v-model="ship.shippingDetail.phone"
                    />
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="country">Country</label>
                    <select
                      required
                      id="country"
                      class="form-select"
                      v-model="ship.shippingDetail.country"
                    >
                      <option selected value="Nigeria">Nigeria</option>
                    </select>
                  </div>
                  <div class="col-lg-6 col-md-12 col-12">
                    <label class="form-label" for="city">City</label>
                    <select
                      required
                      class="form-select"
                      v-model="ship.shippingDetail.city"
                    >
                      <option selected value="city">Select City</option>
                      <option
                        :value="loc.id"
                        v-for="loc in ship.getShippingCostData"
                      >
                        {{ loc.city }}
                      </option>
                    </select>
                  </div>
                  <div class="col-md-12 col-12">
                    <label class="form-label" for="address">Address</label>
                    <input
                      required
                      id="address"
                      class="form-control"
                      v-model="ship.shippingDetail.address"
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
                        v-model="ship.shippingDetail.city"
                        :checked="index === 0 ? true : false"
                      />
                      <label class="form-check-label" :for="'location' + index">
                        {{ location.region }}
                      </label>
                      <span class="float-end ">&#8358; {{ location.cost }}</span>
                    </div>
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
                    <!--div class="input-group-text btn-primary" id="basic" v-show="loading" :disbled="disabled">
                  <span class="spinner-border spinner-border-sm" aria-hidden="true">
                  </span>
                </div-->
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
        <div class="col-xl-3 col-lg-4 col-md-12 col-12">
          <div class="cart-total-area checkout-summary-area">
            <h3 class="d-none d-lg-block mb-0 text-center heading_24 mb-4">
              Order summary
            </h3>
            <div
              class="minicart-item d-flex"
              v-for="(cart, index) in prod.cartItems"
              v-bind:key="index"
            >
              <div class="mini-img-wrapper">
                <img class="mini-img" :src="cart.images[0].img" alt="img" />
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
                <p class="subtotal-value" v-if="!ship.shippingCost[0]">
                  loading
                </p>
                <p class="subtotal-value" v-else>
                  &#x20A6;{{ ship.shippingCost[0].price || 0.0 }}
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
                <p class="subtotal-value" v-if="ship.shippingCost[0]">
                  &#x20A6;{{
                    prod.cartSubtotal +
                    ship.shippingCost[0].price -
                    prod.cartTotalDiscount
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
