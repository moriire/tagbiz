import { computed, reactive, ref } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useShippingStore = defineStore('Shipping', () => {
  const locations = ref([])
  const shippingCost = computed(() => {
    if (shippingDetail.value.delivery_mode === 'ship') {
      let data = locations.value.filter(
        x => x.region === shippingDetail.value.city,
      )
      return data || []
    } else {
      return [{ region: '', cost: 0 }]
    }
  })
  const getShippingCostData = ref([])
  const shippingDetail = ref({
    transaction: {
      metadata: {
        first_name: '',
        last_name: '',
        city: null,
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
      shippingDetail.value.city = res.data[0].region
      shippingDetail.value.cost = res.data[0].cost
      console.log(res.data)
    } catch (e) {
      console.log(e.response)
    }
  }
  const saveOrder = async () => {
    //await getShipping()
    try {
      const res = await axios.put(
        `shipping/${shippingDetail.value.id}`,
        shippingDetail.value,
      )
      //getShippingCostData.value = res.data
      console.log(res)
    } catch (e) {
      console.log(e)
    }
  }

  const addShipping = async product => {
    await getShipping()
    //alert([...wishes.value, product])
    try {
      const res = await axios.post(`shipping`, {
        user: auth.userInfo.pk,
        product: product,
      })
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
    getShipping,
    locations,
  }
})
