<template>
  <body>
    <Header></Header>
    <div class="px-12">
      <div class="flex">
        <div class="w-2/3 bg-gray-300">
          <yandex-map :coords="coords" :settings="settings">
    </yandex-map>
          <div class="bg-green-200">s</div>
        </div>
        <div class="w-1/3 ">
          <div class="px-4">
            <h2 class="text-center font-rale font-bold text-4xl mb-3">
              Последние события
            </h2>
            <div class="px-5">
              <div class=" justify-center mt-2 bg-whitesmoke">
                <div class="px-6 pb-4 text-xl font-rale font-medium">
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Медведев перечислил места нахождения врагов России                 
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Зеленский рассказал о передаче Норвегией Украине 100 миллионов долларов                  
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  На Украине заявили о готовности наносить удары по территории России                   
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Япония заявила о намерении продвигать санкции против России
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  В МИД объявили демарш Финляндии из-за надругательства над российским флагом           
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Минобороны сообщило о занятии выгодных рубежей на краснолиманском направлении                   
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Турция отказалась уступать США в вопросе нефтяных танкеров в ее проливах                   
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  Китай предложил снизить влияние США в нефтяной отрасли                  
                  </a>
                </div>
                <div class="w-full p-2 border-b-2 border-red-300">
                  <a class="text-black hover:text-red-400 transition">
                  В США связали победу Украины с угрозой начала ядерной войны                  
                  </a>
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
