import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import VueAxios from 'vue-axios'
import axios from "axios"
import ElementPlus from "element-plus"

const app = createApp(App).use(VueAxios, axios).use(ElementPlus)

// createApp(App)
//     .use(VueAxios, axios)
//     .use(ElementPlus)
//     .mount('#app')

// app.use(ElementPlus)
app.config.globalProperties.$axios = axios

app.mount('#app')