import { createRouter, createWebHistory } from "vue-router";
import Home from '@/views/Home.vue'


export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Home,
    },
    {
      path: '/pengadaan',
      component: () => import('@/views/Contracts.vue'),
    },
    {
      path: '/perencanaan',
      component: () => import('@/views/Perencanaan.vue'),
    },
    {
      path: '/keuangan',
      component: () => import('@/views/Keuangan.vue'),
    },
    {
      path: '/data',
      component: () => import('@/views/TestData.vue'),
    },
  ]
})
