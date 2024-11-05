import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import router from '@/router'
import alertify from '@/services/alertify'
import { useRouter } from 'vue-router'
import { useShippingStore } from './shipping'


export const useProductStore = defineStore('product', () => {
  const ship = useShippingStore();
  const router = useRouter()
 
const orders = ref({})
const count = ref(0)
const products = ref([])
const similar = ref([])
const product = ref({})
const cartItemsReview = ref([])
const cartItems = ref(JSON.parse(localStorage.getItem("carts")) || []); //ref([])
const cartItemsCount = reactive(JSON.parse(localStorage.getItem("userCartCounter")) || {})
//const cartSubtotal = ref(0)
//const cartTotalDiscount = ref(0)



const getSimilar = async (product_id) => {
  try {
    const res = await axios.get(`api/products/${product_id}/similar`)
    similar.value = res.data
    //pages.items = pages.total/pages.limit;
    console.log(res.data)
  } catch (e) {
    console.log(e)
  }
};

const cartSubtotalReview = computed(() => {
  console.log(cartItemsReview.value)
  let numbers = cartItemsReview.value.map(x => x.cost);
  return numbers.reduce((sum, num) => sum + num, 0);
})

const cartSubtotal = computed(() => {
  console.log(cartItems.value)
  let numbers = cartItems.value.map(x => x.price * x.count);
  return numbers.reduce((sum, num) => sum + num, 0);
})

const cartTotalDiscount = computed(()=>{
  let numbers = cartItems.value.map(x => x.discounted_price * x.count);
  return numbers.reduce((sum, num) => sum + num, 0)
})

const getOrders = async ()=>{
  try {
    const res = await axios.get(`order/${auth.userInfo.id}/get_orders`)
    orders.value = res.data
  } catch(e){
    console.log("Error", e)
  }
}
const addToCartLocal =  (product_obj) => {
    if (cartItems.value.map(x => x.id).includes(product_obj.id)){
      alert("Already in cart");
      return
    } else {
    product_obj["count"] = 1
    cartItems.value.push(product_obj)
    const cartArray = JSON.stringify(cartItems.value)
    localStorage.setItem("carts", cartArray);
    ////getCart()
    return 
    }
}

const deleteCartLocal = async (item) => {
  cartItems.value.pop(item);
  const cartArray = JSON.stringify(cartItems.value);
  localStorage.setItem("carts", cartArray);
  //getCart()
}

const incCartLocal = async () => {
  //getCart();
  //product_obj.count = val;
  console.log(cartItemsCount)
  const cartArray = JSON.stringify(cartItems.value)
    localStorage.setItem("carts", cartArray);
  //getCart()
}

const singeProduct = async (product_id) => {
  try {
    const res = await axios.get(`api/products/${product_id}`)
    product.value = res.data
    //pages.items = pages.total/pages.limit;
    console.log(res.data)
  } catch (e) {
    console.log(e)
  }
};

const addCartForShipping = async (user, product, count) => {
  try {
    const res = await axios.post(`cart`,
      {
          user: auth.userInfo.pk,
          product: product,
          count: count
      }
    )
    //cartContents.value = res.data
    //cartContents.value = res.data
    console.log(res.status)
    //getUserProducts()
  } catch (e) {
    console.log(e)
  }
};

const cartObj = (product, count, user) => {product:product, user=user, count=count}

const cartForShipping = computed(() => {
  return cartItems.value.map(x => 
    {
      return {product: x.id, user: auth.userInfo.pk, count: x.count}
    })
})

const addForShipping = async () => {
  try {
    const res = await axios.post('cart/bulk_cart', cartForShipping.value)
    //cartContents.value = res.data
    //cartContents.value = res.data
    console.log(res)
    ship.saveOrder();
    localStorage.removeItem("userCart")
    setTimeout(() => {
      window.location.href="/orders"
    }, 2000)
    //window.location.href="/orders"
    //getUserProducts()
  } catch (e) {
    console.log(e)
  } 
};
return {
  orders,
  getOrders,
  count,
  product,
  products,
  similar,
  cartItems,
  cartItemsReview,
  cartSubtotal,
  cartTotalDiscount,
  cartSubtotalReview,
  //getCartSubtotal,
  //getCartTotalDiscount,
  addForShipping,
  deleteCartLocal,
  getSimilar,
  singeProduct,
  incCartLocal,
  addToCartLocal,
}
})
