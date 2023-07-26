<template>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg m-2 mt-6">
    <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-6 py-2" v-for="thead in theads" :key="thead.id">
            {{ thead }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
          <!-- <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            Terbayar
          </th> -->
          <td class="px-6 py-2" v-for="tbody in tbodies" :key="tbody.id">
            {{ tbody }}
          </td>
        </tr>
        <!-- <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
          <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
            Kumulatif
          </th>
          <td class="px-6 py-4">
          </td>
        </tr> -->
      </tbody>
    </table>
  </div>
</template>


<script>
export default {
  data() {
    return {
    }
  },
  props: ['theads', 'tbodies']
}
</script>