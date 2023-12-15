import { createApp } from 'vue'
import './style.css'
import App from './App.vue'

import VueAxios from 'vue-axios'
import axios from "axios"
import ElementPlus from "element-plus"
import router from "./router/index.js";
import 'element-plus/dist/index.css'

const app = createApp(App)
app.use(VueAxios, axios)
app.use(ElementPlus)
app.use(router)

// createApp(App)
//     .use(VueAxios, axios)
//     .use(ElementPlus)
//     .mount('#app')

// app.use(ElementPlus)
app.config.globalProperties.$axios = axios

app.mount('#app')