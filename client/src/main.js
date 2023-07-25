import { createApp } from 'vue'
import '@/style.css'
import App from '@/App.vue'
import router from '@/router'
import axios from 'axios'
import "@fortawesome/fontawesome-free/css/all.min.css";


const app = createApp(App)
app.use(router, axios)
app.mount('#app')
