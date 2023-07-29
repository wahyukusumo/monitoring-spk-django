import { createRouter, createWebHistory } from "vue-router";
import Dashboard from '@/views/Dashboard.vue'


export default createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      component: Dashboard,
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
      path: '/pengawas',
      component: () => import('@/views/Pengawas.vue'),
    },
    {
      path: '/data',
      component: () => import('@/views/TestData.vue'),
    },
  ]
})
