<template>
  <body class="bg-idealblack">
    <Header></Header>
    <div class="px-12">
      <div class="flex">
        <div class="w-2/3 mt-14 p-3 border-2 border-red-800">
          <div>
            <yandex-map :coords="coords" :settings="settings" :zoom="5" :cluster-options="clusterOptions">
            <ymap-marker :coords="[47.096701, 65.541300]" marker-type:='Circle' marker-id="666" cluster-name="1"  />
            <ymap-marker :coords="[47.096701, 37.541300]" marker-type:='Circle' marker-id="666" cluster-name="1" />
            <ymap-marker :coords="[47.096701, 45.541300]" marker-type:='Circle' marker-id="666" cluster-name="1" />
            
    </yandex-map>
            <div class="mt-4 grid grid-cols-4 gap-4">
              <div class="bg-whitesmoke"><BarChart></BarChart></div>
              <div class="bg-whitesmoke"><BarChart></BarChart></div>
              <div class="bg-whitesmoke"><BarChart></BarChart></div>
              <div class="bg-whitesmoke"><BarChart></BarChart></div>
            </div>
          </div>
        </div>
        <div class="w-1/3">
          <div class="px-4">
            <h2
              class="text-center font-rale font-bold text-4xl text-whitesmoke mb-3"
            >
              Последние события
            </h2>
            <div class="px-2 border-2 border-red-800">
              <div class="mt-2 bg-idealblack h-screen overflow-y-scroll">
                <div class="px-6 pb-4 text-2xl font-rale font-medium">
                  <div
                    class="w-full p-2 border-b-2 text-whitesmoke hover:text-red-400 border-red-800 hover:border-gray-400 transition"
                  >
                    <p class="hover:none">
                      Медведев перечислил места нахождения врагов России
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
import Header from '../components/Header.vue'
import Footer from '../components/Footer.vue'
import Carousel from '../components/Carousel.vue'
import BarChart from '../components/charts/BarChart.vue'
import { yandexMap, ymapMarker } from 'vue-yandex-maps'
const settings = {
  apiKey: '06856716-badb-42a6-9815-4c8e630af04b',
  lang: 'ru_RU',
  coordorder: 'latlong',
  enterprise: false,
  version: '2.1'
}

export default {
  components: { Header, Footer, Carousel, yandexMap, ymapMarker, BarChart },

  data () {
    return {
      coords: [55.753215, 37.622504], 
      settings: settings,
      clusterOptions: {
      1: {
        clusterDisableClickZoom: true,
        clusterOpenBalloonOnClick: true,
        clusterBalloonLayout: [
          '<ul class=list>',
          '{% for geoObject in properties.geoObjects %}',
          '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
          '{% endfor %}',
          '</ul>',
        ].join(''),
      },
    },
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
