import 'aos/dist/aos.css'
import "bootstrap/dist/css/bootstrap.min.css"
import "./assets/css/style.css"
import "@fortawesome/fontawesome-free/css/all.min.css"
import "bootstrap/dist/js/bootstrap.bundle.min.js"
import "bootstrap/dist/js/bootstrap.min.js"
import "@fortawesome/fontawesome-free/js/all.min.js"
//import "./assets/js/vendor.js"
//import "./assets/js/main.js"

import "alertifyjs/build/css/alertify.min.css"

import AOS from 'aos';
import { createApp } from 'vue'
import { createPinia } from 'pinia'
import axios from "axios"
import App from './App.vue'
import router from './router'

//axios.defaults.baseURL="http://127.0.0.1:8000/"
axios.defaults.baseURL= import.meta.env.VITE_BACKEND
//"https://tagbiz.pythonanywhere.com/"

const app = createApp(App)
app.use(createPinia())
app.use(router)
AOS.init()
app.mount('#app')
