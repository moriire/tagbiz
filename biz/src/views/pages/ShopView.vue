<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue'
//import LoaderSpinner from "@/components/LoaderSpinner.vue"
import { useRoute } from 'vue-router'
import ProductPage from '@/components/ProductPage.vue'
import { useProductStore } from '@/stores/products'
import { useFilterStore } from '@/stores/filter'
const prod = useProductStore()
const filter = useFilterStore()
const route = useRoute()
const loading = ref(true)
const items = ref([])
const pagination = ref({
  count: 0,
  next: null,
  previous: null,
})
const limit = 8 
const offset = ref(0)
onMounted(async () => {
  await fetchItems()
})
const fetchItems = async (url = null) => {
  try {
    const apiUrl = url || `api/products/?limit=${limit}&offset=${offset}`
    const response = await axios.get(apiUrl)
    items.value = response.data.results
    pagination.value.count = response.data.count
    pagination.value.next = response.data.next
    pagination.value.previous = response.data.previous

    // Update offset for the next page
    if (response.data.next) {
      const urlParams = new URLSearchParams(new URL(response.data.next).search)
      offset.value = parseInt(urlParams.get('offset'), 10)
    }
  } catch (error) {
    console.error('Error fetching items:', error)
  }
}
</script>

<template>
  <!--teleport to="#app">
      <LoaderSpinner :loading="loading" />
    </teleport-->
  <div class="collection mt-100">
    <div class="container">
      <div class="row">
        <!-- product area start -->
        <div class="col-lg-12 col-md-12 col-12">
          <div
            class="filter-sort-wrapper d-flex justify-content-between flex-wrap"
          >
            <div class="collection-title-wrap d-flex align-items-end">
              <h2 class="collection-title heading_24 mb-0">All products</h2>
              <p class="collection-counter text_16 mb-0 ms-2">
                ({{ items.length }} items)
              </p>
            </div>
            <div class="filter-sorting">
              <div
                class="collection-sorting position-relative d-none d-lg-block"
              >
                <div
                  class="sorting-header text_16 d-flex align-items-center justify-content-end"
                >
                  <span class="sorting-title me-2">Sort by:</span>
                  <span class="active-sorting">Featured</span>
                  <span class="sorting-icon">
                    <svg
                      uclass="icon icon-down"
                      xmlns="http://www.w3.org/2000/svg"
                      width="24"
                      height="24"
                      viewBox="0 0 24 24"
                      fill="none"
                      stroke="currentColor"
                      stroke-width="2"
                      stroke-linecap="round"
                      stroke-linejoin="round"
                      class="feather feather-chevron-down"
                    >
                      <polyline points="6 9 12 15 18 9"></polyline>
                    </svg>
                  </span>
                </div>
                <ul class="sorting-lists list-unstyled m-0">
                  <li><a href="#" class="text_14">Featured</a></li>
                  <li><a href="#" class="text_14">Best Selling</a></li>
                  <li><a href="#" class="text_14">Alphabetically, A-Z</a></li>
                  <li><a href="#" class="text_14">Alphabetically, Z-A</a></li>
                  <li><a href="#" class="text_14">Price, low to high</a></li>
                  <li><a href="#" class="text_14">Price, high to low</a></li>
                  <li><a href="#" class="text_14">Date, old to new</a></li>
                  <li><a href="#" class="text_14">Date, new to old</a></li>
                </ul>
              </div>
              <div
                class="filter-drawer-trigger mobile-filter d-flex align-items-center d-lg-none"
              >
                <span class="mobile-filter-icon me-2">
                  <svg
                    xmlns="http://www.w3.org/2000/svg"
                    width="24"
                    height="24"
                    viewBox="0 0 24 24"
                    fill="none"
                    stroke="currentColor"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                    class="icon icon-filter"
                  >
                    <polygon
                      points="22 3 2 3 10 12.46 10 19 14 21 14 12.46 22 3"
                    ></polygon>
                  </svg>
                </span>
                <span class="mobile-filter-heading">Sorting</span>
              </div>
            </div>
          </div>
          <ProductPage :products="items" :show="true" />

      <div class="pagination justify-content-center mt-100" >
        <!-- Pagination Controls -->
        <nav>
          <ul class="pagination ">
            <li class="page-item p-2" :class="{ disabled: !pagination.previous }">
              <button
                class="btn btn-primary"
                @click="fetchItems(pagination.previous)"
                :disabled="!pagination.previous"
              >
                Previous
              </button>
            </li>
            <li class="page-item p-2" :class="{ disabled: !pagination.next }">
              <button
                class="btn btn-primary"
                @click="fetchItems(pagination.next)"
                :disabled="!pagination.next"
              >
                Next
              </button>
            </li>
          </ul>
        </nav>
        <!-- Pagination Controls -->
      </div>
        </div>
        <!-- product area end -->

        <!--ShopSidebar /-->
      </div>
    </div>
  </div>
</template>
