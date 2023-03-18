<template>
  <body class="bg-idealblack">
    <Header></Header>
    <div class="sm:px-3 sm:pt-2">
      <div class="flex flex-col">
        <div class="w-full border-b-red-500 border-b">
          <div class="sm:px-4 sm:mb-10">
            <div class=" text-black sm:px-24 px-4">
              <div class="flex justify-between items-center mb-2 sm:pb-2 sm:mt-2 mt-2">
                <span class="sm:text-3xl text-lg text-whitesmoke font-mono rounded-lg"
                  >Выбранный БПЛА: <span class="underline font-bold"> {{ choosed_uav }} </span></span
                >
                <select
                  class="sm:px-6 px-2 text-idealblack sm:text-lg text-sm rounded-lg sm:w-1/3 w-1/2 mr-2 sm:mr-8 sm:p-2 p-1"
                  v-model="selected"
                >
                  <option class="" disabled value="">Выберите страну</option>
                  <option v-for="country in allCountries" :key="country">
                    {{ country }}
                  </option>
                </select>
              </div>
              <div
                class="sm:mb-10 grid grid-cols-1 sm:grid-cols-4 sm:h-[52rem] h-[40rem] overflow-y-scroll"
              >
                <UAVCard
                  v-for="card in allUAVS"
                  :key="card.id"
                  v-model="choosed_range"
                  @click="click_drone(card.name, card.range_, card.max_speed)"
                  :uav_img="card.picture"
                  :uav_company="card.company"
                  :uav_country="card.country"
                  :uav_endurance="card.endurance"
                  :uav_max_speed="card.max_speed"
                  :uav_name="card.name"
                  :uav_payload="card.payload"
                  :uav_range="card.range_"
                ></UAVCard>
              </div>
            </div>
          </div>
        </div>
        <div class="w-full sm:px-28">
          <div class="sm:px-1 px-4 py-2 sm:py-1">
            <h2
              class="text-center sm:mt-6 mt-2 font-monster sm:text-4xl text-2xl text-whitesmoke sm:mb-8 mb-3"
            >
              Область применения
            </h2>
            <Map></Map>
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
import UAVCard from "../components/UAVCard.vue";
import Map from "../components/Map.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: { Header, Footer, Map, UAVCard },
  data() {
    return {
      choosed_uav: "",
      choosed_range: 0,
      current_icon: '',
      selected: ''

    };
  },
  computed: mapGetters(["allCountries", "allUAVS"]),
  methods: {
    ...mapActions(["GET_ALLCOUNTRIES", "CHANGE_UAV", "CHANGE_RANGE", "CHANGE_ICON", "GET_ALLUAVS"]),
    click_drone(uav, range, max_speed) {
      this.choosed_uav = uav;
      this.choosed_range = range;
      this.CHANGE_UAV(uav);
      this.CHANGE_RANGE(range);
      if (0 <= max_speed && max_speed < 92.6){
        this.current_icon = 'https://cdn-icons-png.flaticon.com/512/974/974510.png'
      }
      else if (92.6 <= max_speed &&  max_speed < 463){
        this.current_icon = 'https://cdn-icons-png.flaticon.com/512/2792/2792018.png'
      }
      else {
        this.current_icon = 'https://cdn-icons-png.flaticon.com/512/2223/2223188.png'
      }
      this.CHANGE_ICON(this.current_icon);
    },
  },
  async created() {
    this.GET_ALLUAVS()
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
