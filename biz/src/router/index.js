import { createRouter,  createWebHashHistory  } from 'vue-router'
import HomeView from '@/views/pages/HomeView.vue'
import ProductDetail from '@/views/pages/ProductDetail.vue'
import CartView from '@/views/pages/CartView.vue'
import CheckoutView from '@/views/pages/CheckoutView.vue'
import SuccessView from '../views/pages/SuccessView.vue'
import CategoryPageView from '@/views/pages/CategoryPageView.vue'
import ShopView from '@/views/pages/ShopView.vue'
import PagesBase from '../views/PagesBase.vue'
import { useLoader } from '../composables/useLoader.js';
const { showLoader, hideLoader } = useLoader();

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
          component: HomeView,
          meta: { title: `Welcome` }
        },
        {
          path: 'product/:product',
          name: 'product-detail',
          component: ProductDetail,
          meta: { title: `Products` }
        },
        {
          path: 'category/:categories_slug',
          name: 'categories',
          component: CategoryPageView,
          meta: { title: `Products in category` }
        },
        {
          path: '/cart',
          name: 'cart',
          component: CartView,
          meta: { title: "Cart" }
        },
        {
          path: '/checkout',
          name: 'checkout',
          component: CheckoutView,
          meta: { title: "Pay Securely" }
        },
        {
          path: '/orders',
          name: 'orders',
          component: () => import('@/views/pages/OrderReview.vue'),
          meta: { title: "Orders" }
        },
        {
          path: '/payment-success',
          name: 'payment-success',
          component: SuccessView,
          meta: { title: "Payment Success" }
        },
        {
          path: 'shop',
          name: 'shop',
          component: ShopView,
          meta: { title: "Trending Products" }
        },
        {
          path: '/about',
          name: 'about',
          component: () => import('../views/pages/ContactView.vue'),
          meta: { title: "About Us" }
        },
        {
          path: '/contact',
          name: 'contact',
          component: () => import('../views/pages/ContactView.vue'),
          meta: { title: "Contact Us" }
        },
      ],
      component: PagesBase
    }
  ]
})

router.beforeEach((to, from, next) => {
  showLoader();
  next();
});

router.afterEach((to) => {
  document.title = `Tagbiz | ${to.meta.title}`
  console.log(router.value)
  setTimeout(() => hideLoader(), 500); 
})
export default router