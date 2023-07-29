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
            Pembayaran
          </th>
          <th scope="col" class="px-6 py-3">
            Tanggal Pembayaran
          </th>
          <th scope="col" class="px-6 py-3">
            Nilai
          </th>
          <th scope="col" class="px-6 py-3">
            Keterangan
          </th>
          <th scope="col" class="px-6 py-3">
            Action
          </th>
        </tr>
      </thead>
      <tbody>
        <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700" v-for="payment in payments"
          :key="payment.index">
          <th scope="row" class="px-6 py-4 font-bold text-gray-900 whitespace-nowrap dark:text-white">
            {{ payment.nomor_spk.nomor_spk }}
          </th>
          <td class="px-6 py-4">
            {{ payment.pembayaran }}
          </td>
          <td class="px-6 py-4">
            {{ payment.tanggal_pembayaran }}
          </td>
          <td class="px-6 py-4">
            Rp.{{ payment.nilai }}
          </td>
          <td class="px-6 py-4">
            {{ payment.keterangan }}
          </td>
          <td class="px-6 py-4">
            <!-- Add modal -->
            <FormModal modal-title="Add New Payment" button-text="Add Payment">
              <template v-slot:body>
                <form v-on:submit.prevent="submitForm(payment)">

                  <TextInput :label="'Nomor SPK'">
                    <input type="text" name="no_spk" id="no_spk" v-model="payment.nomor_spk_id" :class="textInputClass"
                      placeholder=" " required />
                  </TextInput>
                  <TextInput :label="'Pembayaran'">
                    <input type="text" name="pembayaran" id="pembayaran" v-model="addPayment.pembayaran" :class="textInputClass"
                      placeholder=" " required />
                  </TextInput>
                  <TextInput :label="'Nilai'">
                    <input type="number" name="nilai" id="nilai" v-model="addPayment.nilai"
                      :class="textInputClass" placeholder=" " required />
                  </TextInput>
                  <TextInput :label="'Tanggal Pembayaran'">
                    <input type="date" name="tanggal_pembayaran" id="tanggal_pembayaran" v-model="addPayment.tanggal_pembayaran"
                      :class="textInputClass" placeholder=" " required />
                  </TextInput>
                  <TextInput :label="'Keterangan'">
                    <input type="text" name="keterangan" id="keterangan" v-model="addPayment.keterangan" :class="textInputClass"
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
      payments: [''],
      addPayment: {
        pembayaran: '',
        nilai: undefined,
        tanggal_pembayaran: undefined,
        keterangan: ''
      },
      textInputClass: 'block py-2.5 px-0 w-full text-sm text-gray-900 bg-transparent border-0 border-b-2 border-gray-300 appearance-none dark:text-white dark:border-gray-600 dark:focus:border-blue-500 focus:outline-none focus:ring-0 focus:border-blue-600 peer'
    }
  },
  methods: {
    async getData() {
      try {
        // fetch payments
        const response = await axios.get(
          'http://127.0.0.1:8000/api/keuangan/'
        );
        // set the data returned as payments
        this.payments = response.data;
      } catch (error) {
        // log the error
        console.log(error);
      }
    },
    async submitForm(payment) {
      try {
        // Send a POST request to the API
        const response = await axios.post('http://127.0.0.1:8000/api/keuangan/', {
          nomor_spk_id: this.payment.nomor_spk_id,
          pembayaran: this.addPayment.pembayaran,
          nilai: this.addPayment.nilai,
          tanggal_pembayaran: this.addPayment.tanggal_pembayaran,
          keterangan: this.addPayment.keterangan,
        });
        // Append the returned data to the tasks array
        this.payments.push(response.data);
        // Reset the title and description field values.
        this.addPayment.nomor_spk_id = '';
        this.addPayment.pembayaran = '';
        this.addPayment.nilai = '';
        this.addPayment.tanggal_pembayaran = '';
        this.addPayment.keterangan = '';
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