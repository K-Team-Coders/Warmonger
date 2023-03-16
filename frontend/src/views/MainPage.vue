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
                <option v-for="country in allCountries" :key="country">
                  {{ country }}
                </option>
              </select>
              <div class="mt-4 h-screen">
                <UAVCard
                  v-for="card in allUAVS"
                  :key="card.id"
                  v-model="choosed_range"
                  @click="click_drone(card.name, card.range)"
                  :uav_company="card.company"
                  :uav_country="card.country"
                  :uav_endurance="card.endurance"
                  :uav_max_speed="card.max_speed"
                  :uav_name="card.name"
                  :uav_payload="card.payload"
                  :uav_range="card.range"
                ></UAVCard>
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
import UAVCard from "../components/UAVCard.vue";
import Map from "../components/Map.vue";
import { mapActions, mapGetters } from "vuex";
export default {
  components: { Header, Footer, Map, UAVCard },
  data() {
    return {
      choosed_uav: "",
      choosed_range: 0,
    };
  },
  computed: mapGetters(["allCountries", "allUAVS"]),
  methods: {
    ...mapActions(["GET_ALLCOUNTRIES", "CHANGE_UAV", "CHANGE_RANGE"]),
    click_drone(uav, range) {
      this.choosed_uav = uav;
      this.choosed_range = range;
      this.CHANGE_UAV(uav);
      this.CHANGE_RANGE(range)
    },
  },
  async created() {
    console.log(this.allCountries);
    console.log(this.allUAVS)
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
