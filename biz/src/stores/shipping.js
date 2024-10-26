import { computed, reactive, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useShippingStore = defineStore('Shipping', () => {
  const locations = ref([])
  const shippingCost = computed( ()=>{
    let data = getShippingCostData.value.filter(x => x.id === shippingDetail.value.city);
    return data
})
  const getShippingCostData = ref([])
  const shippingDetail = ref({
    first_name: "",
    last_name: "",
    city: null,
    email: "",
    country: "Nigeria",
    address: "",
    phone: "",
    created_by: null,
  });

  const getShipping = async () => {
    try {
      const res = await axios.get('api/locations/')
      locations.value = res.data
      //shippingDetail.value.city = res.data.data.city
      //console.log(shippingDetail)
    } catch (e) {
      console.log(e.response)
    }
  }
  const getShippingCost = async () => {
    try {
      const res = await axios.get('shipping-cost')
      getShippingCostData.value = res.data
    } catch (e) {
      console.log(e.response)
    }
  };
  const saveOrder = async () => {
    //await getShipping()
    try {
      const res = await axios.put(`shipping/${shippingDetail.value.id}`, shippingDetail.value)
      //getShippingCostData.value = res.data
      console.log(res)
    } catch (e) {
      console.log(e)
    }
  }

  const addShipping = async (product) => {
    await getShipping()
    //alert([...wishes.value, product])
    try {
      const res = await axios.post(`shipping`,
        {
          user: auth.userInfo.pk,
          product: product
        }
      )
      //wishes.value = res.data
      //wishes.value = res.data
      console.log(res.data)
      //getUserProducts()
    } catch (e) {
      console.log(e)
    }
  }

  return {
    shippingDetail,
    shippingCost,
    getShippingCostData,
    saveOrder,
    getShippingCost,
    getShipping,
    locations
  }
})
