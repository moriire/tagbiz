import { reactive, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"



export const useWishlistStore = defineStore('cartlist', () => {
  const auth = useAuthStore();
  const cartContents = ref([]);
  
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
      console.log(res.data)
      //getUserProducts()
    } catch (e) {
      console.log(e)
    }
  }

  return {
    productData,
    addCartForShipping,
    cartContents
  }
})
