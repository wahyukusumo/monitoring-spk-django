<template>
  <div class="grid grid-cols-3 gap-4 mb-4">
    <div class="flex flex-col items-center justify-center rounded bg-gray-50 dark:bg-gray-800 p-5">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Basket Keandalan</h5>
      <div class="w-60">
        <Pie id="my-chart-id" :options="chartOptions" :data="chartsData[0]" />
      </div>
      <DashboardTable :theads="['Terbayar', 'Terkontrak']" :tbodies="['Rp.50.000.000', 'Rp.70.000.000']" />
    </div>
    <div class="flex flex-col items-center justify-center rounded bg-gray-50 dark:bg-gray-800 p-5">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Basket Efisiensi</h5>
      <div class="w-60">
        <Pie id="my-chart-id" :options="chartOptions" :data="chartsData[1]" />
      </div>
      <DashboardTable :theads="['Terbayar', 'Terkontrak']" :tbodies="['Rp.12.000.000', 'Rp.40.000.000']" />
    </div>
    <div class="flex flex-col items-center justify-center rounded bg-gray-50 dark:bg-gray-800 p-5">
      <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Basket Pemasaran</h5>
      <div class="w-60">
        <Pie id="my-chart-id" :options="chartOptions" :data="chartsData[2]" />
      </div>
      <DashboardTable :theads="['Terbayar', 'Terkontrak']" :tbodies="['Rp.20.000.000', 'Rp.40.000.000']" />
    </div>
  </div>
  <div class="flex flex-col items-center justify-center h-96 mb-4 rounded bg-gray-50 dark:bg-gray-800">
    <!-- <h5 class="mb-2 text-2xl font-bold tracking-tight text-gray-900 dark:text-white">Pembayaran Tahun Ini</h5> -->
    <Line id="my-chart-full" :options="chartOptions" :data="chartsData[3]" />
  </div>

  <div class="flex flex-col items-center justify-center mb-4 rounded bg-gray-50 dark:bg-gray-800 p-3">
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg">
      <table class="w-full text-sm text-left text-gray-500 dark:text-gray-400">
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
          <tr>
            <th scope="col" class="px-6 py-3">
              <i class="fa-solid fa-chart-simple"></i>
            </th>
            <th scope="col" class="px-3 py-3" v-for="month in chartsData[3].labels">
              {{ month }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
              {{ chartsData[3].datasets[1].label }}
            </th>
            <td class="px-3 py-4" v-for="data in chartsData[3].datasets[1].data">
              Rp.{{ data }}
            </td>
          </tr>
          <tr class="bg-white border-b dark:bg-gray-800 dark:border-gray-700">
            <th scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
              {{ chartsData[3].datasets[0].label }}
            </th>
            <td class="px-3 py-4" v-for="data in chartsData[3].datasets[0].data">
              Rp.{{ data }}
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import { Bar, Pie, Line } from 'vue-chartjs'
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Colors, ArcElement, PointElement, LineElement} from 'chart.js'
import DashboardTable from '../components/DashboardTable.vue'


ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, PointElement, LineElement, Colors, ArcElement)

export default {
  components: { Bar, Pie, DashboardTable, Line },
  data() {
    return {
      chartsData: [
        {
          labels: ['Terkontrak', 'Terbayar'],
          datasets: [
            {
              data: [70000000, 50000000],
              backgroundColor: [
                'rgba(255, 205, 86, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgba(255, 205, 86, 0.2)',
                'rgb(201, 203, 207)'
              ],
            }
          ]
        },
        {
          labels: ['Terkontrak', 'Terbayar'],
          datasets: [
            {
              data: [40000000, 12000000],
              backgroundColor: [
                'rgba(54, 162, 235, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(54, 162, 235)',
                'rgb(201, 203, 207)'
              ],
            }
          ]
        },
        {
          labels: ['Terkontrak', 'Terbayar'],
          datasets: [
            {
              data: [40000000, 20000000],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(201, 203, 207)'
              ],
            }
          ]
        },
        {
          labels: ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'],
          datasets: [
            {
              label: 'Kumulatif',
              data: [10000000, 34000000, 50000000, 65000000, 80000000, 124000000, 220000000, 230000000, 255000000, 260000000, 300000000, 310000000],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
              ],
              borderWidth: 1,
            },
            {
              label: 'Terbayar',
              data: [50000000, 20000000, 30000000, 55000000, 10000000, 11000000, 180000000, 190000000, 250000000, 220000000, 150000000, 300000000],
              backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(255, 205, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(201, 203, 207, 0.2)'
              ],
              borderColor: [
                'rgb(255, 99, 132)',
                'rgb(255, 159, 64)',
                'rgb(255, 205, 86)',
                'rgb(75, 192, 192)',
                'rgb(54, 162, 235)',
                'rgb(153, 102, 255)',
                'rgb(201, 203, 207)'
              ],
              borderWidth: 1,
            }
          ]
        }
      ],
      chartOptions: {
        responsive: true,
      }
    }
  }
}
</script>