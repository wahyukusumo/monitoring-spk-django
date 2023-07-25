<template>
  <div class="flex items-center justify-between pb-4">
    <div class="pt-1">
      <button type="button" @click="addModalShow = true"
        class="px-5 py-2.5 text-sm font-medium text-white inline-flex items-center bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 rounded-lg text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800">
        <i class="fa-solid fa-plus mr-3"></i>
        Add New Contract
      </button>
    </div>
    <Search />
  </div>

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
            <button @click="updateContract(contract)"
              class="mx-2 font-medium text-blue-600 dark:text-blue-500 hover:underline">Edit</button>
            <button @click="deleteContract(contract)"
              class="mx-2 font-medium text-red-600 dark:text-red-500 hover:underline">Delete</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>

  <!-- Add modal -->
  <FormModal :modal-show="addModalShow" :modal-title="'Add New Contract'"
    @closeApp="this.addModalShow = !this.addModalShow">
    <template v-slot:body>
      <form v-on:submit.prevent="submitForm">

        <TextInput :label="'Nomor SPK'">
          <input type="text" name="no_spk" id="no_spk" v-model="addContract.nomor_spk" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Vendor'">
          <input type="text" name="vendor" id="vendor" v-model="addContract.vendor" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Mulai'">
          <input type="date" name="tanggal_mulai" id="tanggal_mulai" v-model="addContract.tanggal_mulai"
            :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Akhir'">
          <input type="date" name="tanggal_akhir" id="tanggal_akhir" v-model="addContract.tanggal_akhir"
            :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Uraian'">
          <input type="text" name="uraian" id="uraian" v-model="addContract.uraian" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Nilai'">
          <input type="text" name="nilai" id="nilai" v-model="addContract.nilai" :class="textInputClass" placeholder=" "
            required />
        </TextInput>
        <TextInput :label="'Basket'">
          <input type="text" name="basket" id="basket" v-model="addContract.basket" :class="textInputClass"
            placeholder=" " required />
        </TextInput>

        <div>
          <button type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
            Submit
          </button>
          <button type="reset"
            class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
            Reset
          </button>
        </div>

      </form>
    </template>
  </FormModal>

  <!-- Edit modal -->
  <FormModal :modal-show="editModalShow" :modal-title="'Edit Contract'"
    @closeApp="this.editModalShow = !this.editModalShow">
    <template v-slot:body>
      <form v-on:submit.prevent="submitForm">

        <TextInput :label="'Nomor SPK'">
          <input type="text" name="no_spk" id="no_spk" v-model="editContract.nomor_spk" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Vendor'">
          <input type="text" name="vendor" id="vendor" v-model="editContract.vendor" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Mulai'">
          <input type="date" name="tanggal_mulai" id="tanggal_mulai" v-model="editContract.tanggal_mulai"
            :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Tanggal Akhir'">
          <input type="date" name="tanggal_akhir" id="tanggal_akhir" v-model="editContract.tanggal_akhir"
            :class="textInputClass" placeholder=" " required />
        </TextInput>
        <TextInput :label="'Uraian'">
          <input type="text" name="uraian" id="uraian" v-model="editContract.uraian" :class="textInputClass"
            placeholder=" " required />
        </TextInput>
        <TextInput :label="'Nilai'">
          <input type="text" name="nilai" id="nilai" v-model="editContract.nilai" :class="textInputClass" placeholder=" "
            required />
        </TextInput>
        <TextInput :label="'Basket'">
          <input type="text" name="basket" id="basket" v-model="editContract.basket" :class="textInputClass"
            placeholder=" " required />
        </TextInput>

        <div>
          <button type="submit"
            class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800">
            Submit
          </button>
          <button type="reset"
            class="text-gray-900 bg-white border border-gray-300 focus:outline-none hover:bg-gray-100 focus:ring-4 focus:ring-gray-200 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-gray-800 dark:text-white dark:border-gray-600 dark:hover:bg-gray-700 dark:hover:border-gray-600 dark:focus:ring-gray-700">
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
import Search from '../components/Search.vue';

import axios from 'axios';

export default {
  data() {
    return {
      addModalShow: false,
      editModalShow: false,
      contracts: [''],
      addContract: {
        nomor_spk: '',
        vendor: '',
        tanggal_mulai: undefined,
        tanggal_akhir: undefined,
        uraian: '',
        nilai: undefined,
        basket: '',
      },
      editContract: {
        nomor_spk: '',
        vendor: '',
        tanggal_mulai: undefined,
        tanggal_akhir: undefined,
        uraian: '',
        nilai: undefined,
        basket: '',
      },
      textInputClass: 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'
    }
  },
  methods: {
    async getData() {
      try {
        // fetch contracts
        const response = await axios.get(
          'http://127.0.0.1:8000/api/pengadaan/'
        );
        // set the data returned as contracts
        this.contracts = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async getDataSearch() {
      try {
        // fetch contracts
        const response = await axios.get(
          'http://127.0.0.1:8000/api/pengadaan/search/'
        );
        // set the data returned as contracts
        this.contracts = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async updateContract(contract) {
      this.editModalShow = !this.editModalShow
      try {

        // Send a request to API to update the contract
        const response = await axios.put(`http://127.0.0.1:8000/api/pengadaan/${contract.id}/`, {
          nomor_spk: contract.nomor_spk,
          vendor: contract.vendor,
          tanggal_mulai: contract.tanggal_mulai,
          tanggal_akhir: contract.tanggal_akhir,
          uraian: contract.uraian,
          nilai: contract.nilai,
          basket: contract.basket,
        });

        // Get the index of the task being updated
        let contractIndex = this.contracts.findIndex(t => t.id === contract.id);

        // Reset the contracts array with the new data of the updated task
        this.contracts = this.contracts.map((contract) => {
          if (this.contracts.findIndex(t => t.id === contract.id) === contractIndex) {
            return response.data;
          }
          return contract;
        });

      } catch (error) {

        // Log any error
        console.log(error);
      }
    },
    async deleteContract(contract) {

      // Confirm if one wants to delete the contract
      let confirmation = confirm("Do you want to delete this task?");

      if (confirmation) {
        try {

          // Send a request to delete the contract
          await axios.delete(`http://127.0.0.1:8000/api/pengadaan/${contract.id}`);

          // Refresh the contracts
          this.getData();
        } catch (error) {

          // Log any error
          console.log(error)
        }
      }
    },
    async submitForm() {
      try {
        // Send a POST request to the API
        const response = await axios.post('http://127.0.0.1:8000/api/pengadaan/', {
          nomor_spk: this.addContract.nomor_spk,
          vendor: this.addContract.vendor,
          tanggal_mulai: this.addContract.tanggal_mulai,
          tanggal_akhir: this.addContract.tanggal_akhir,
          uraian: this.addContract.uraian,
          nilai: this.addContract.nilai,
          basket: this.addContract.basket,
        });
        // Append the returned data to the tasks array
        this.contracts.push(response.data);
        // Reset the title and description field values.
        this.addContract.nomor_spk = '';
        this.addContract.vendor = '';
        this.addContract.tanggal_mulai = '';
        this.addContract.tanggal_akhir = '';
        this.addContract.uraian = '';
        this.addContract.nilai = '';
        this.addContract.basket = '';
      } catch (error) {
        // Log the error
        console.log(error);
      }
    },
  },
  created() {
    this.getData()
  },
  components: {
    TextInput,
    FormModal,
    Search
  }
}
</script>