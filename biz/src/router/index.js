import { createRouter,  createWebHashHistory  } from 'vue-router'
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
          component: () => import('../views/pages/HomeView.vue')
        },
        {
          path: 'product/:product',
          name: 'product-detail',
          component: () => import('../views/pages/ProductDetail.vue')
        },
        {
          path: ':categories_slug',
          name: 'categories',
          component: () => import('../views/pages/CategoryPageView.vue')
        },
        {
          path: '/cart',
          name: 'cart',
          component: () => import('../views/pages/CartView.vue'),
          //meta: { requiresAuth: true }
        },
        {
          path: '/checkout',
          name: 'checkout',
          component: () => import('../views/pages/CheckoutView.vue'),
          meta: { requiresAuth: true }
        },
        {
          path: '/orders',
          name: 'orders',
          component: () => import('../views/pages/OrderReview.vue'),
          meta: { requiresAuth: true }
        },
        {
          path: '/payment-success',
          name: 'payment-success',
          component: () => import('../views/pages/SuccessView.vue'),
          meta: { requiresAuth: true }
        },
        {
          path: 'shop',
          name: 'shop',
          component: () => import('../views/pages/ShopView.vue'),
          // meta: { requiresAuth: true }
        },
        {
          path: '/about',
          name: 'about',
          component: () => import('../views/pages/AboutView.vue')
        },
      ],
      component: () => import('../views/PagesBase.vue')
    }
  ]
})

export default router
