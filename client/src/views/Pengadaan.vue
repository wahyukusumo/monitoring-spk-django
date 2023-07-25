<template>
  <div class="flex items-center justify-between pb-4">
    <div class="pt-1">
      <button type="button" @click="modalShow = true"
        class="px-5 py-2.5 text-sm font-medium text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        <i class="fa-solid fa-plus mr-3"></i>
        Add New Contract
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

  <TableContracts :contract="contract" />

  <!-- Main modal -->
  <FormModal :modal-show="modalShow" :modal-title="'Add New Contract'" @closeApp="this.modalShow = !this.modalShow">
    <template v-slot:body>
      <form v-on:submit.prevent="submitForm">

        <TextInput :label="'Nomor SPK'">
          <input type="text" name="no_spk" id="no_spk" v-model="nomor_spk" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Vendor'">
          <input type="text" name="vendor" id="vendor" v-model="vendor" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Mulai'">
          <input type="date" name="tanggal_mulai" id="tanggal_mulai" v-model="tanggal_mulai" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Akhir'">
          <input type="date" name="tanggal_akhir" id="tanggal_akhir" v-model="tanggal_akhir" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Uraian'">
          <input type="text" name="uraian" id="uraian" v-model="uraian" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Nilai'">
          <input type="text" name="nilai" id="nilai" v-model="nilai" :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Basket'">
          <input type="text" name="basket" id="basket" v-model="basket" :class="textInputClass" placeholder=" " required />
        </TextInput>

        <div>
          <button type="submit" class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
            Submit
          </button>
          <button type="reset" class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
            Reset
          </button>
        </div>

      </form>
    </template>
  </FormModal>
</template>


<script>
import FormModal from '../components/FormModal.vue';
import TextInput from '../components/Forms/TextInput.vue';
import TableContracts from '../components/TableContracts.vue';

import axios from 'axios';

export default {
  data() {
    return {
      modalShow: false,
      contract: [''],
      nomor_spk: '',
      vendor: '',
      tanggal_mulai: undefined,
      tanggal_akhir: undefined,
      uraian: '',
      nilai: undefined,
      basket: '',
      textInputClass: 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'
    }
  },
  methods: {
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await axios.post('http://127.0.0.1:8000/api/pengadaan/', {
          nomor_spk: this.nomor_spk,
          vendor: this.vendor,
          tanggal_mulai: this.tanggal_mulai,
          tanggal_akhir: this.tanggal_akhir,
          uraian: this.uraian,
          nilai: this.nilai,
          basket: this.basket,
        });
        // Append the returned data to the tasks array
        this.contract.push(response.data);
        // Reset the title and description field values.
        this.nomor_spk = '';
        this.vendor = '';
        this.tanggal_mulai = '';
        this.tanggal_akhir = '';
        this.uraian = '';
        this.nilai = '';
        this.basket = '';
      } catch (error) {
        // Log the error
        console.log(error);
      }
    },
  },
  created() {
  },
  components: {
    TableContracts,
    TextInput,
    FormModal
  }
}
</script>