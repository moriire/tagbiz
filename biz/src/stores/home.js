import { ref, computed, reactive } from 'vue'
import { defineStore } from 'pinia'
import axios from "axios"


export const useHomeStore = defineStore('home', () => {
    const latests = ref([])
    const discounteds = ref([])
    const promotions = ref([])
    const getLatest = async () => {
        try {
            const res = await axios.get(`api/products/`)
            latests.value = res.data
            console.log(res.data)
        } catch (e) {
            console.log(e)
        }
    }

    const getDiscounted = async () => {
        try {
            const res = await axios.get(`api/products/`)
            discounteds.value = res.data
            console.log(res.data)
        } catch (e) {
            console.log(e)
        }
    }

    const getPromoted = async () => {
        try {
            const res = await axios.get(`api/products/`)
            console.log(res.data)
            promotions.value = res.data
        } catch (e) {
            console.log(e)
        }
    }

    
    return {
        getLatest,
        latests,
        getDiscounted,
        discounteds,
        getPromoted,
        promotions

    }
})