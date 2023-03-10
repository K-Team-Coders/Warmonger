<template>
  <yandex-map
    :coords="coords"
    :settings="settings"
    :zoom="5"
    :cluster-options="clusterOptions"
  >
    <!-- <ymap-marker 
      :coords="coords" 
      marker-id="123" 
      hint-content="some hint" 
    /> -->
    <ymap-marker
      v-for="uav in allUAVs"
      :key="uav.id"
      marker-type="circle"
      :marker-id="uav.id"
      :coords="uav.coords"
      :marker-fill="markerfill"
      :marker-stroke="markerstroke"
      circle-radius="1000000"
    />
  </yandex-map>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
const settings = {
  apiKey: '06856716-badb-42a6-9815-4c8e630af04b',
  lang: 'ru_RU',
  coordorder: 'latlong',
  enterprise: false,
  version: '2.1'
}

export default {
    components: { yandexMap, ymapMarker },
    computed: mapGetters(["allUAVs"]),
  data() {
    return {
      coords: [55.753215, 46.622504],
      settings: settings,
      markerfill: {
        enabled: true,
        color: "#DB4521",
        opacity: 0.8
      },
      markerstroke: {
color: "#ffffff",
opacity: 0.8,
 width: 5
      },
    }},
    methods: {
      mapActions(['createCountriesList']),
      async mounted(){
        this.createCountriesList();
      }
    }

  }
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>
