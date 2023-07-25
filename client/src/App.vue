<template>
  <button @click="showSideBar = !showSideBar" data-drawer-target="separator-sidebar" data-drawer-toggle="separator-sidebar" aria-controls="separator-sidebar"
    type="button"
    class="inline-flex items-center p-2 mt-2 ml-3 text-sm text-gray-500 rounded-lg sm:hidden hover:bg-gray-100 focus:outline-none focus:ring-2 focus:ring-gray-200 dark:text-gray-400 dark:hover:bg-gray-700 dark:focus:ring-gray-600">
    <span class="sr-only">Open sidebar</span>
    <svg class="w-6 h-6" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20" xmlns="http://www.w3.org/2000/svg">
      <path clip-rule="evenodd" fill-rule="evenodd"
        d="M2 4.75A.75.75 0 012.75 4h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 4.75zm0 10.5a.75.75 0 01.75-.75h7.5a.75.75 0 010 1.5h-7.5a.75.75 0 01-.75-.75zM2 10a.75.75 0 01.75-.75h14.5a.75.75 0 010 1.5H2.75A.75.75 0 012 10z">
      </path>
    </svg>
  </button>

  <aside id="separator-sidebar" v-show="showSideBar"
    class="fixed top-0 left-0 z-40 w-64 h-screen transition-transform -translate-x-full sm:translate-x-0"
    aria-label="Sidebar">
    <div class="h-full px-3 py-4 overflow-y-auto bg-gray-50 dark:bg-gray-800">
      <ul class="space-y-2 font-medium">

        <router-link to="/">
          <SidebarList :name="'Dashboard'">
            <i class="fa-solid fa-chart-pie" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="/pengadaan">
          <SidebarList :name="'Pengadaan'">
            <i class="fa-solid fa-file-lines" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="/perencanaan">
          <SidebarList :name="'Perencanaan'">
            <i class="fa-solid fa-map" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="/pengawas-jaringan">
          <SidebarList :name="'Pengawas Jaringan'">
            <i class="fa-solid fa-network-wired" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="transaksi-energi">
          <SidebarList :name="'Transaksi Energi'">
            <i class="fa-solid fa-bolt" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="pengawas-konstruksi">
          <SidebarList :name="'Pengawas Konstruksi'">
            <i class="fa-solid fa-helmet-safety" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="keuangan">
          <SidebarList :name="'Keuangan'">
            <i class="fa-solid fa-coins" :class="iconClass"></i>
          </SidebarList>
        </router-link>

      </ul>

      <ul class="pt-4 mt-4 space-y-2 font-medium border-t border-gray-200 dark:border-gray-700">
        <router-link to="user">
          <SidebarList :name="'User'">
            <i class="fa-solid fa-user" :class="iconClass"></i>
          </SidebarList>
        </router-link>

        <router-link to="log-out">
          <SidebarList :name="'Logout'">
            <i class="fa-solid fa-right-from-bracket" :class="iconClass"></i>
          </SidebarList>
        </router-link>
      </ul>
    </div>
  </aside>

  <div class="p-4 sm:ml-64">
    <div class="p-4 border-2 border-gray-200 border-dashed rounded-lg dark:border-gray-700">
      <router-view />
    </div>
  </div>
</template>

<script>
import SidebarList from '@/components/SidebarList.vue';

export default {
  data() {
    return {
      showSideBar: true,
      iconClass: 'text-gray-500 transition duration-75 dark:text-gray-400 group-hover:text-gray-900 dark:group-hover:text-white'
    };
  },
  methods: {
  },
  components: {
    SidebarList
  },
};
</script>

<!-- <template>
  <div id="app">
    <router-view />
  </div>
</template> -->
