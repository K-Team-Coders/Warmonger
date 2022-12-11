<template>
<body>
<Header></Header>
<div class="px-20">
  <div class="flex">
    <div class="w-2/3 bg-gray-300">ss
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
export default {
  components: {Header,Footer,Carousel}
}
</script>

<style>

</style>
