<template>
    <yandex-map :coords="coords" :settings="settings" :zoom="5" :cluster-options="clusterOptions">
              <ymap-marker v-for="item in maplocations" :key="item.id" :coords="[item.latitude, item.longitude]"
                :marker-id="item.id" :cluster-name="1" :balloon="{ header: item.adress }" />
            </yandex-map>
</template>

<script>
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
data() {
    return {
      chartData1: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [
          {
            label: 'Топ локаций по событиям',
            backgroundColor: '#ba4949',
            data: [40, 20, 12, 45, 42]
          }
        ]
      },
      chartData2: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [
          {
            label: 'Топ персон по событиям',
            backgroundColor: '#a8b6de',
            data: [40, 20, 12, 75, 87]
          }
        ]
      },
      chartData3: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [
          {
            label: 'Топ организаций по событиям',
            backgroundColor: '#982e48',
            data: [40, 20, 12, 45, 42]
          }
        ]
      },
      chartData4: {
        labels: ['1', '2', '3', '4', '5'],
        datasets: [
          {
            label: 'Топ тегов по событиям',
            backgroundColor: '#efdcce',
            data: [40, 20, 12, 45, 42]
          }
        ]
      },
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