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
              <ymap-marker v-for="item in maplocations" :key="item.id" :coords="[item.latitude, item.longitude]"
                :marker-id="item.id" :cluster-name="1" :balloon="{ header: item.adress }" />

            </yandex-map>
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
                      {{ item.id }}) {{ item.title }}
                    </p>
                    <p>{{ item.text }}</p>

                  </div>
                </div>
              </div>

            </div>

          </div>

        </div>

      </div>
      <div class="bg-whitesmoke text-gray-900 font-base text-3xl mb-2 font-rale text-center border-b ">
        <p class="border-b text-whitesmoke mb-3 border-red-800">Граф отношений событий</p>
        <svg width="960" height="600" class="container-border"></svg>
      </div>
    </div>

    <Footer></Footer>
  </body>
</template>

<script>
import * as d3 from 'd3'
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
        }),
      axios.get('http://127.0.0.1:8000/main/getNewsRelations/')
        .then(response => {
          let nodes2 = response.data.nodes
          console.log(nodes2)
          let edges = response.data.relations
          console.log(edges)
          let marge = { top: 60, bottom: 60, left: 60, right: 60 }
          let svg = d3.select('svg')
          let width = svg.attr('width')
          let height = svg.attr('height')
          let g = svg.append('g')
            .attr('transform', 'translate(' + marge.top + ',' + marge.left + ')')
          // Node Dataset
          // Side Dataset
          // 边集
          // Set a color scale
          // 设置一个颜色比例尺
          let colorScale = d3.scaleOrdinal()
            .domain(d3.range(nodes2.length))
            .range(d3.schemeCategory10)
          // Create a new force guide diagram
          // 新建一个力导向图
          let forceSimulation = d3.forceSimulation()
            .force('link', d3.forceLink())
            .force('charge', d3.forceManyBody())
            .force('center', d3.forceCenter())
          // Generate node data
          // 生成节点数据
          forceSimulation.nodes(nodes2)
            .on('tick', ticked)
          // Generate side data
          // 生成边数据
          forceSimulation.force('link')
            .links(edges)
            .distance(function (d) { // side length / 每一边的长度
              return d.value * 100
            })
          // Set drawing center location
          forceSimulation.force('center')
            .x(width / 2)
            .y(height / 2)
          // Draw side
          let links = g.append('g')
            .selectAll('line')
            .data(edges)
            .enter()
            .append('line')
            .attr('stroke', function (d, i) {
              return colorScale(i)
            })
            .attr('stroke-width', 1)
          // Text on side
          let linksText = g.append('g')
            .selectAll('text')
            .data(edges)
            .enter()
            .append('text')
            .text(function (d) {
              return d.relation
            })
          // Create group
          let gs = g.selectAll('.circleText')
            .data(nodes2)
            .enter()
            .append('g')
            .attr('transform', function (d) {
              let cirX = d.x
              let cirY = d.y
              return 'translate(' + cirX + ',' + cirY + ')'
            })
            .call(d3.drag()
              .on('start', started)
              .on('drag', dragged)
              .on('end', ended)
            )
          // Draw node
          gs.append('circle')
            .attr('r', 10)
            .attr('fill', function (d, i) {
              return colorScale(i)
            })
          // Draw text
          gs.append('text')
            .attr('x', -10)
            .attr('y', -20)
            .attr('dy', 10)
            .text(function (d) {
              return d.name
            })
          // ticked
          function ticked() {
            links
              .attr('x1', function (d) { return d.source.x })
              .attr('y1', function (d) { return d.source.y })
              .attr('x2', function (d) { return d.target.x })
              .attr('y2', function (d) { return d.target.y })
            linksText
              .attr('x', function (d) { return (d.source.x + d.target.x) / 2 })
              .attr('y', function (d) { return (d.source.y + d.target.y) / 2 })
            gs
              .attr('transform', function (d) { return 'translate(' + d.x + ',' + d.y + ')' })
          }
          // drag
          function started(d) {
            if (!d3.event.active) {
              forceSimulation.alphaTarget(0.8).restart() // Set the attenuation coefficient to simulate the node position movement process. The higher the value, the faster the movement. The value range is [0, 1] // 设置衰减系数，对节点位置移动过程的模拟，数值越高移动越快，数值范围[0, 1]
            }
            d.fx = d.x
            d.fy = d.y
          }
          let zoomHandler = d3.zoom()
            .on('zoom', zoomActions)
          zoomHandler(svg)
          function zoomActions() {
            g.attr('transform', d3.event.transform)
          }
          function dragged(d) {
            d.fx = d3.event.x
            d.fy = d3.event.y
          }
          function ended(d) {
            if (!d3.event.active) {
              forceSimulation.alphaTarget(0)
            }
            d.fx = null
            d.fy = null
          }
        }) 
},
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