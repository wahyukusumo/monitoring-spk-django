<template>
  <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
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
          <th scope="col" class="px-6 py-3">
            Action
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="contract in contracts"
          :key="contract.index">
          <th scope="row" class="px-6 py-4 font-bold text-gray-900 whitespace-nowrap dark:text-white">
            {{ contract.nomor_spk }}
          </th>
          <td class="px-6 py-4">
            {{ contract.vendor }}
          </td>
          <td class="px-6 py-4">
            {{ contract.tanggal_mulai }}
          </td>
          <td class="px-6 py-4">
            {{ contract.tanggal_akhir }}
          </td>
          <td class="px-6 py-4">
            {{ contract.uraian }}
          </td>
          <td class="px-6 py-4">
            Rp.{{ contract.nilai }}
          </td>
          <td class="px-6 py-4">
            {{ contract.basket }}
          </td>
          <td class="px-6 py-4">
            <slot name="table-action"></slot>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      contracts: ['']
    }
  },
  props: ['contracts']
}
</script>