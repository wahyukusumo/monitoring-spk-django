<template>
  <div class="flex items-center justify-between pb-4">
    <div class="pt-1">
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
            <!-- Add modal -->
            <FormModal modal-title="Approve Contract" button-text="Approve">
              <template v-slot:body>
                <form v-on:submit.prevent="updateContract(contract)">
                  <TextInput :label="'Nomor SPK'">
                    <input type="text" name="no_spk" id="no_spk" v-model="contract.nomor_spk" :class="textInputClass"
                      placeholder=" " disabled />
                  </TextInput>
                  <TextInput :label="'Vendor'">
                    <input type="text" name="vendor" id="vendor" v-model="contract.vendor" :class="textInputClass"
                      placeholder=" " disabled />
                  </TextInput>
                  <TextInput :label="'Tanggal Mulai'">
                    <input type="date" name="tanggal_mulai" id="tanggal_mulai" v-model="contract.tanggal_mulai"
                      :class="textInputClass" placeholder=" " disabled />
                  </TextInput>
                  <TextInput :label="'Tanggal Akhir'">
                    <input type="date" name="tanggal_akhir" id="tanggal_akhir" v-model="contract.tanggal_akhir"
                      :class="textInputClass" placeholder=" " disabled />
                  </TextInput>
                  <TextInput :label="'Uraian'">
                    <input type="text" name="uraian" id="uraian" v-model="contract.uraian" :class="textInputClass"
                      placeholder=" " disabled />
                  </TextInput>
                  <TextInput :label="'Nilai'">
                    <input type="text" name="nilai" id="nilai" v-model="contract.nilai" :class="textInputClass" placeholder=" "
                      disabled />
                  </TextInput>
                  <TextInput :label="'Basket'">
                    <input type="text" name="basket" id="basket" v-model="contract.basket" :class="textInputClass"
                      placeholder=" " disabled />
                  </TextInput>

                  <hr class="h-px my-8 bg-gray-200 border-0 dark:bg-gray-500">

                  <div class="relative z-0 w-full mb-6 group">
                    <label for="bagian" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">Pilih Bagian</label>
                    <select id="bagian" v-model="this.bagian" class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
                      <option>Jaringan</option>
                      <option>Konstruksi</option>
                      <option>Transaksi Energi</option>
                    </select>
                  </div>
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

          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import FormModal from '../components/FormModal.vue';
import TextInput from '../components/Forms/TextInput.vue';
import Search from '../components/Search.vue';

import axios from 'axios';

export default {
  data() {
    return {
      contracts: [''],
      bagian: '',
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
    async updateContract(contract) {
      try {
        // Send a request to API to update the contract
        const response = await axios.put(`http://127.0.0.1:8000/api/pengadaan/${contract.id}/`, {
          bagian: this.bagian
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