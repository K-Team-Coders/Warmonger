<template>
  <body class="bg-idealblack">
    <Header></Header>
    <div class="px-12 pt-16">
      <div class="flex">
        <div class="w-2/3 border border-gray-50">
          <div class="px-1 border border-gray-50">
            <h2
              class="text-center font-rale font-bold text-4xl text-whitesmoke mb-3"
            >
              Карта
            </h2>
            <Map></Map>
          </div>
        </div>
        <div class="w-1/3 border border-gray-50">
          <div class="px-4 border border-gray-50">
            <h2
              class="text-center font-rale font-bold text-4xl text-whitesmoke mb-3"
            >
              Приспешники
            </h2>
            <div
              class="px-2 border-opacity-80 border text-black border-gray-50"
            >
              <select
                class="px-6 mt-2 text-idealblack border border-gray-100 text-lg rounded-lg block w-full p-2"
                v-model="selected"
              >
                <option disabled value="">Выберите страну</option>
                <option v-for="country in allCountries" :key="country"> {{country}}</option>
              </select>
              <div class="mt-4 h-screen">
                <div
                  class="flex justify-center pb-2 items-center text-sm font-rale font-medium"
                >
                  <div class="flex flex-col justify-between p-3 hover:bg-sky-70 leading-normal">
                    <p class="text-lg font-bold tracking-tight text-white">
                      General Atomics MQ-1C Grey Eagle
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Страна: Америкосы
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Коммисия: 1000$
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Дальность, км: 1800
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Нагрузка, кг: 1000
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Макс.скорость, км/ч: 120
                    </p>
                    <p class="mb-1 font-normal text-gray-200 border-b-2">
                      Выносливость: 1000
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from "../components/Header.vue";
import Footer from "../components/Footer.vue";
import Graph from "../components/Graph.vue";
import BarChart from "../components/charts/BarChart.vue";
import Map from "../components/Map.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: { Header, Footer, BarChart, Map, Graph },
  computed: mapGetters(["allCountries"]),
  methods: mapActions(["GET_ALLCOUNTRIES"]),
  async created(){
      this.GET_ALLCOUNTRIES()
      console.log(this.allCountries)
    }
  }
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
