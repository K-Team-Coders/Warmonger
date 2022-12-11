<template>

  <body>
    <Header></Header>
    <div class="px-20">
      <div class="flex">
        <div class="w-2/3 bg-gray-300">
          <yandex-map :coords="coords" :settings="settings">
    </yandex-map>
          <div class="w-full bg-green-200">s</div>
        </div>
        <div class="w-1/3 bg-red-200 ">s</div>
      </div>

    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import Carousel from '../components/Carousel.vue'
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
const settings = {
  apiKey: '06856716-badb-42a6-9815-4c8e630af04b',
  lang: 'ru_RU',
  coordorder: 'latlong',
  enterprise: false,
  version: '2.1'
}

export default {
  components: { Header, Footer, Carousel, yandexMap, ymapMarker},

  data(){
    return {
      coords: [55.753215, 37.622504],
      settings: settings
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
