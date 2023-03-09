<template>

  <body class="bg-idealblack">
    <Header></Header>
    <div class="px-12 pt-16">
      <div class="flex">
        <div class="w-2/3">
          <div class="px-1">
            <h2 class="text-center font-rale font-bold text-4xl text-whitesmoke mb-3">
              Карта событий
            </h2>
            <Map> </Map>
            <div class="mt-4 grid grid-cols-4 gap-4">
              <div class="bg-white">
                <BarChart :chartData="chartData1"></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart :chartData="chartData2"></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart :chartData="chartData3"></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart :chartData="chartData4"></BarChart>
              </div>
            </div>
          </div>
        </div>
        <div class="w-1/3">
          <div class="px-4">
            <h2 class="text-center font-rale font-bold text-4xl text-whitesmoke mb-3">
              Последние события
            </h2>
            <div class="px-2 border-opacity-80 border-2 border-red-800">
              <!-- <select id="countries"
                class="px-6 mt-2 text-idealblack border-red-900 border-2 text-lg rounded-lg block w-full p-2">
                <option selected>Выберите тему </option>
                <option>Путин</option>
                <option>Путин</option>
                <option>Путин</option>
              </select> -->
              <div class="mt-2 bg-idealblack h-screen overflow-y-scroll">
                <div class="px-6 pb-4 text-sm font-rale font-medium">
                  <div v-for="item in news" :key='item.id'
                    class=" w-full p-2 border-b-2 text-whitesmoke hover:text-red-400 border-red-800 hover:border-gray-400 transition">
                    <p class="font-bold">{{ item.date }}</p>
                    <p>
                      {{ item.id }} {{ item.title }}
                    </p>
                    <p>{{ item.text }}</p>

                  </div>
                </div>
              </div>

            </div>

          </div>

        </div>

      </div>
      <p class="flex justify-center text-gray-900 font-base text-3xl mb-2 font-rale text-center border-b text-whitesmoke mb-3 border-red-800">Граф отношений событий</p>
      <div class="flex justify-center text-gray-900 font-base text-3xl mb-2 font-rale text-center border-b ">
     <Graph></Graph>
      </div>
    </div>

    <Footer></Footer>
  </body>
</template>

<script>

import axios from 'axios'
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import Graph from '../components/Graph.vue'
import BarChart from '../components/charts/BarChart.vue'
import Map from '../components/Map.vue'




export default {
  components: { Header, Footer,  BarChart, Map, Graph },

  
  mounted() {
    axios
      .get('http://127.0.0.1:8000/main/getAllNews/?format=json')
      .then(response => {
        response.data.forEach(
          element => {
            this.news.push(element)
            element.locations.forEach(
              subelement => {
                this.maplocations.push(subelement)
              }
            )
          }
        );
        console.log(this.news)
      }),
      axios.get('http://127.0.0.1:8000/main/topNews/')
        .then(response => {
          this.chartData1.labels = response.data.locations_label
          this.chartData1.datasets[0].data = response.data.location_count

          this.chartData2.labels = response.data.persons_labels
          this.chartData2.datasets[0].data = response.data.persons_count

          this.chartData3.labels = response.data.organizations_labels
          this.chartData3.datasets[0].data = response.data.organizations_count

          this.chartData4.labels = response.data.tag_labels
          this.chartData4.datasets[0].data = response.data.tag_count
        })},
methods: {
  sendid(itemid) {
    console.log(itemid)
    axios
      .get('http://127.0.0.1:8000/main/getDetailNews/' + itemid + '/?format=json')
      .then(response => {
        this.maplocations = this.maplocations.splice(0, this.maplocations.length)
        console.log(this.maplocations)

      }
      )
  },
  showall_news(){
    axios
      .get('http://127.0.0.1:8000/main/getAllNews/?format=json')
      .then(response => {
        response.data.forEach(
          element => {
            this.news.push(element)
            element.locations.forEach(
              subelement => {
                this.maplocations.push(subelement)
              }
            )
          }
        );
        console.log(this.news)
      })
  }
}}

</script>

<style>


.shake {
  animation: shake 0.82s cubic-bezier(0.36, 0.07, 0.19, 0.97) both;
  transform: translate3d(0, 0, 0);
}

@keyframes shake {

  10%,
  90% {
    transform: translate3d(-1px, 0, 0);
  }

  20%,
  80% {
    transform: translate3d(2px, 0, 0);
  }

  30%,
  50%,
  70% {
    transform: translate3d(-4px, 0, 0);
  }

  40%,
  60% {
    transform: translate3d(4px, 0, 0);
  }
}
</style>