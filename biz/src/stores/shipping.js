import { computed, reactive, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useShippingStore = defineStore('Shipping', () => {
  const locations = ref([])
  //const shippingCostData = ref(0)
  const shippingCostData = computed(() => locations.value.filter(
        x => x.region === shippingDetail.value.transaction.metadata.city,
      )[0]
    )
/*
  const updateShippingCost = () => {
      let data =  locations.value.filter(
        x => x.region === shippingDetail.value.transaction.metadata.city,
      )
      shippingCostData.value = data[0].cost
    
  }
      */
  const shippingDetail = ref({
    transaction: {
      metadata: {
        first_name: '',
        last_name: '',
        city: null,
        cost: 0,
        email: '',
        country: 'Nigeria',
        address: '',
        phone: '',
        created_by: null,
        delivery_mode: 'ship',
        custom_fields: [],
      },
      amount: 0,
      email: '',
    },
  })

  const getShipping = async () => {
    try {
      const res = await axios.get('api/locations/')
      locations.value = res.data
      shippingDetail.value.transaction.metadata.city = res.data[0].region
      //console.log(res.data)
    } catch (e) {
      console.log(e.response)
    }
  }

  return {
    shippingDetail,
    //shippingCost,
    shippingCostData,
    getShipping,
    locations,
    //updateShippingCost
  }
})
