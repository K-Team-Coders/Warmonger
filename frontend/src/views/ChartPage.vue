<template>
  <body>
    <section class="bg-dark-gray">
      <Header></Header>
      <div class="relative grid grid-cols-2 grid-rows-2 px-4 gap-4 h-auto ">
        <div class="bg-white rounded-2xl shadow-2xl shadow-white scale-95">
          <div class="px-5 py-3">
            <BarChart :chart-data="chartDataBar"></BarChart>
            <div class="flex justify-center ">
              <button
                type="button"
                @click="BarChart_DataLoading()"
                class=" flex justify-center px-24 py-3 mt-20 bg-red-600 text-white font-medium font-rale text-lg leading-tight uppercase rounded shadow-md hover:bg-red-900 hover:shadow-lg focus:bg-green-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-green-800 active:shadow-lg transition duration-150 ease-in-out"
              >
                Загрузить
              </button>
            </div>
          </div>
        </div>
        <div class="px-4 py-1">
          <div class="bg-white rounded-2xl  shadow-2xl shadow-white scale-95">
            <RadarChart :chart-data="chartDataRadar"></RadarChart>
            <div class="flex justify-center pb-3 pt-5">
              <button
                type="button"
                @click="RadarChart_DataLoading()"
                class=" flex justify-center px-24 py-3 bg-red-600 text-white font-medium text-lg font-rale leading-tight uppercase rounded shadow-md hover:bg-red-900 hover:shadow-lg focus:bg-green-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-green-800 active:shadow-lg transition duration-150 ease-in-out"
              >
                Загрузить
              </button>
            </div>
          </div>
        </div>
        <div
          class="bg-white rounded-2xl shadow-2xl shadow-white pt-36 col-start-1 col-end-3 scale-95"
        >
          <div class="px-5">
            <ScatterChart :chart-data="chartDataScatter"></ScatterChart>
            <div class="flex justify-center pb-3 pt-5">
              <button
                type="button"
                @click="ScatterChart_DataLoading()"
                class=" flex justify-center px-24 py-3 bg-red-600 text-white font-medium text-lg font-rale leading-tight uppercase rounded shadow-md hover:bg-red-900 hover:shadow-lg focus:bg-green-700 focus:shadow-lg focus:outline-none focus:ring-0 active:bg-green-800 active:shadow-lg transition duration-150 ease-in-out"
              >
                Загрузить
              </button>
            </div>
          </div>
        </div>
      </div>
      <Footer></Footer>
    </section>
  </body>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import BarChart from '../components/charts/BarChart.vue'
import RadarChart from '../components/charts/RadarChart.vue'
import D3BarChart from '../components/charts/D3BarChart.vue'
import ScatterChart from '../components/charts/ScatterChart.vue'
import axios from 'axios'
export default {
  components: {
    Header,
    Footer,
    BarChart,
    RadarChart,
    D3BarChart,
    ScatterChart
  },
  data () {
    return {
      chartDataScatter: {
        datasets: [
          {
            label: 'Random',
            fill: false,
            borderColor: '#887BB5',
            backgroundColor: '#4528A4',
            data: [{ x: 23, y: 234 }]
          },
          
          
        ]
      },
      chartDataBar: {
        labels: [ 'JOIN', 'SELECT', 'March'],
        datasets: [
          {
            label: 'Random',
            backgroundColor: '#293857',
            data: [40, 20, 12]
          }
        ]
      },
      chartDataRadar: {
        labels: ['Eating','Drinking','Sleeping','Designing','Coding', 'Cycling', 'Running'],
      datasets: [
        {
          label: 'Random2   ',
          backgroundColor: 'rgba(179,181,198,0.2)',
          borderColor: 'rgba(179,181,198,1)',
          pointBackgroundColor: 'rgba(179,181,198,1)',
          pointBorderColor: '#fff',
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: 'rgba(179,181,198,1)',
          data: [65, 59, 90, 81, 56, 55, 40]
        }
      ]
      },   
    }
  },
  methods: {
    ScatterChart_DataLoading () {
        console.log('working')
        axios.get('http://127.0.0.1:8000/main/testdata/').then(response => {
                console.log(response.data)
                let x = response.data.x
                let y = response.data.y
                console.log(response.data.pack)
                let pack = response.data.pack 
                this.$data.chartDataScatter.datasets[0].data = pack
                }
            )
        },
    BarChart_DataLoading()  {
        axios.get('http://127.0.0.1:8000/main/testdata2/').then(response => {
                console.log(response.data)
                let x = response.data.x
                let label = response.data.labels
                this.$data.chartDataBar.datasets[0].data = x
                this.$data.chartDataBar.labels = label
                }
            )
        },
    RadarChart_DataLoading() {
        axios.get('http://127.0.0.1:8000/main/testdata3/').then(response => {
                console.log(response.data)
                let x = response.data.x
                let label = response.data.labels
                this.$data.chartDataRadar.labels = label
                this.$data.chartDataRadar.data.datasets[0].data = x
            }
        )
    }
  }
}
</script>

<style></style>
