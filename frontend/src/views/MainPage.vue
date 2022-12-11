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
            <yandex-map :coords="coords" :settings="settings" :zoom="5" :cluster-options="clusterOptions">
              <ymap-marker v-for="item in news" :key="item.id"
                :coords='[item.locations.latitude, item.locations.longitude]' :marker-id="item.id"
                :cluster-name="item.cluster" />
              
            </yandex-map>
            <div class="mt-4 grid grid-cols-4 gap-4">
              <div class="bg-white">
                <BarChart></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart></BarChart>
              </div>
              <div class="bg-whitesmoke">
                <BarChart></BarChart>
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
              <select id="countries"
                class="px-6 mt-2 text-idealblack border-red-900 border-2 text-lg rounded-lg block w-full p-2">
                <option selected>Выберите тему </option>
                <option>Путин</option>
                <option>Путин</option>
                <option>Путин</option>
              </select>
              <div class="mt-2 bg-idealblack h-screen overflow-y-scroll">
                <div class="px-6 pb-4 text-2xl font-rale font-medium">
                  <div @click="sendid()" v-for="item in news" :key='item.id'
                    class=" w-full p-2 border-b-2 text-whitesmoke hover:text-red-400 border-red-800 hover:border-gray-400 transition">
                    <p class="font-bold">{{ item.date }}</p>
                    <p class="">
                      {{ item.title }}
                    </p>
                    <p>{{ item.text }}</p>

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
import axios from 'axios'
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

  data() {
    return {
      coords: [55.753215, 37.622504],
      settings: settings,
      newsEnabled: false,

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
      tags: [{ id: '', name: '' }],
      news: [
        {
          id: 1,
          title: '',
          text: '',
          date: '',
          locations: [
            {
              id: '',
              name: '',
              latitude: '',
              longitude: '',
              adress: '',
            }
          ],
          persons: [
            {
              id: '',
              name: '',
              nickname: ''
            }
          ],
          organizations: [
            {
              id: '',
              name: ''
            }
          ],
          tags: {
            id: '',
            name: ''
          },
          source: '',
          cluster: '1',
        },
      ],
      current_news: [
            {
              id: '',
              name: '',
              latitude: '',
              longitude: '',
              adress: '',
            }
          ]
    }
  },
  mounted() {
    axios
      .get('http://127.0.0.1:8000/main/getAllNews/?format=json')
      .then(response => {
        response.data.forEach(element => this.news);
        console.log(this.news)
      })
  },
  methods: {
    sendid() {
      axios
        .post('http://127.0.0.1:8000/main/getAllNews/?format=json', this.news[0].id)
        .then(response => {
          console.log(this.news.id)
          
          this.current_news.latitude = response.data[45].locations[0].latitude
          this.current_news.longitude = response.data[45].locations[0].longitude
        }
        )
    }
  }
}
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}

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
