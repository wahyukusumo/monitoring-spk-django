<template>
  <div class="flex items-center justify-between pb-4">
    <div>
      <button type="button"
        class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
        Input Data
      </button>
    </div>
    <label for="table-search" class="sr-only">Search</label>
    <div class="relative">
      <div class="absolute inset-y-0 left-0 flex items-center pl-3 pointer-events-none">
        <svg class="w-5 h-5 text-gray-500 dark:text-gray-400" aria-hidden="true" fill="currentColor" viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
            d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
            clip-rule="evenodd"></path>
        </svg>
      </div>
      <input type="text" id="table-search"
        class="block p-2 pl-10 text-sm text-gray-900 border border-gray-300 rounded-lg w-80 bg-gray-50 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"
        placeholder="Search for items">
    </div>
  </div>
  <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
    <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
      <tr>
        <th scope="col" class="px-6 py-3">
          No. SPK
        </th>
        <th scope="col" class="px-6 py-3">
          Vendor
        </th>
        <th scope="col" class="px-6 py-3">
          Awal SPK
        </th>
        <th scope="col" class="px-6 py-3">
          Akhir SPK
        </th>
        <th scope="col" class="px-6 py-3">
          Uraian
        </th>
        <th scope="col" class="px-6 py-3">
          Nilai
        </th>
        <th scope="col" class="px-6 py-3">
          Basket
        </th>
      </tr>
    </thead>
    <tbody>
      <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700 hover:bg-gray-50 dark:hover:bg-gray-600"
        v-for="task in tasks" :key="task.index">
        <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
          {{ task.nomor_spk }}
        </th>
        <td class="px-6 py-4">
          {{ task.vendor }}
        </td>
        <td class="px-6 py-4">
          {{ task.tanggal_mulai }}
        </td>
        <td class="px-6 py-4">
          {{ task.tanggal_akhir }}
        </td>
        <td class="px-6 py-4">
          {{ task.uraian }}
        </td>
        <td class="px-6 py-4">
          Rp.{{ task.nilai }}
        </td>
        <td class="px-6 py-4">
          {{ task.basket }}
        </td>
        <td class="px-6 py-4">
          <a href="#" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</a>
        </td>
      </tr>
    </tbody>
  </table>
  <nav class="flex items-center justify-between pt-4" aria-label="Table navigation">
    <span class="text-sm font-normal text-gray-500 dark:text-gray-400">Showing <span
        class="font-semibold text-gray-900 dark:text-white">1-10</span> of <span
        class="font-semibold text-gray-900 dark:text-white">1000</span></span>
    <ul class="inline-flex -space-x-px text-sm h-8">
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 ml-0 leading-tight text-gray-500 bg-white border border-gray-300 rounded-l-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Previous</a>
      </li>
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">1</a>
      </li>
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">2</a>
      </li>
      <li>
        <a href="#" aria-current="page"
          class="flex items-center justify-center px-3 h-8 text-blue-600 border border-gray-300 bg-blue-50 hover:bg-blue-100 hover:text-blue-700 dark:border-gray-700 dark:bg-gray-700 dark:text-white">3</a>
      </li>
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">4</a>
      </li>
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">5</a>
      </li>
      <li>
        <a href="#"
          class="flex items-center justify-center px-3 h-8 leading-tight text-gray-500 bg-white border border-gray-300 rounded-r-lg hover:bg-gray-100 hover:text-gray-700 dark:bg-gray-800 dark:border-gray-700 dark:text-gray-400 dark:hover:bg-gray-700 dark:hover:text-white">Next</a>
      </li>
    </ul>
  </nav>
</template>


<script>
import axios from 'axios';

export default {
  data() {
    return {
      // tasks
      tasks: ['']
    }
  },
  methods: {
    async getData() {
      try {
        // fetch tasks
        const response = await axios.get(
          "http://127.0.0.1:8000/api/pengadaan/"
        );
        // set the data returned as tasks
        this.tasks = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
  },
  created() {
    // Fetch tasks on page load
    this.getData();
  }
}
</script>