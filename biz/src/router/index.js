import { createRouter,  createWebHashHistory  } from 'vue-router'
import HomeView from '@/views/pages/HomeView.vue'
import ProductDetail from '@/views/pages/ProductDetail.vue'
import CartView from '@/views/pages/CartView.vue'
import CheckoutView from '@/views/pages/CheckoutView.vue'
import SuccessView from '../views/pages/SuccessView.vue'
import CategoryPageView from '@/views/pages/CategoryPageView.vue'
import ShopView from '@/views/pages/ShopView.vue'
import PagesBase from '../views/PagesBase.vue'
const router = createRouter({
  history: createWebHashHistory("/tagbiz/"),
  linkActiveClass: 'active',
  linkExactActiveClass: 'active',
  routes: [
    {
      path: '/',
      name: 'pages',
      children: [
        {
          path: '',
          name: 'home',
          component: HomeView
        },
        {
          path: 'product/:product',
          name: 'product-detail',
          component: ProductDetail
        },
        {
          path: ':categories_slug',
          name: 'categories',
          component: CategoryPageView
        },
        {
          path: '/cart',
          name: 'cart',
          component: CartView,
          //meta: { requiresAuth: true }
        },
        {
          path: '/checkout',
          name: 'checkout',
          component: CheckoutView,
          meta: { requiresAuth: true }
        },
        {
          path: '/orders',
          name: 'orders',
          component: () => import('@/views/pages/OrderReview.vue'),
          meta: { requiresAuth: true }
        },
        {
          path: '/payment-success',
          name: 'payment-success',
          component: SuccessView,
          meta: { requiresAuth: true }
        },
        {
          path: 'shop',
          name: 'shop',
          component: ShopView
          // meta: { requiresAuth: true }
        },
        {
          path: '/about',
          name: 'about',
          component: () => import('../views/pages/AboutView.vue')
        },
      ],
      component: PagesBase.vue
    }
  ]
})

export default router
