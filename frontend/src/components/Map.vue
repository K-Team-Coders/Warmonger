<template>
    <yandex-map :coords="coords" :settings="settings" :zoom="5" :cluster-options="clusterOptions">
             <!-- <ymap-marker 
      :coords="coords" 
      marker-id="123" 
      hint-content="some hint" 
    /> -->
              <ymap-marker v-for="uav in allUAVs" :key="uav.id" marker-type="circle" :marker-id="uav.id" :coords="uav.coords" :marker-fill="markerfill" :marker-stroke="markerstroke" circle-radius="1000000" />
            </yandex-map>
</template>

<script>
import {mapGetters} from 'vuex'
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
      tags: [{ id: '', name: '' }],
      maplocations: [
        {
          id: '',
          name: '',
          latitude: '',
          longitude: '',
          adress: '',
        }
      ],
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
}
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
</style>