<template>
  <body class="bg-idealblack">
    <Header></Header>
    <div class="xl:px-3 xl:pt-2">
      <div class="flex flex-col">
        <div class="w-full border-b-red-500 border-b">
          <div class="xl:px-4 sm:px-2 xl:mb-10 sm:mb-4">
            <div class=" text-black xl:px-24 px-4">
              <div class="flex justify-between items-center mb-2 xl:pb-2 xl:mt-2 mt-2">
              
              
              </div>
            </div>
          </div>
        </div>
        <div class="w-full sm:px-12 sm:p-2 2xl:px-28">
          <div class="xl:px-1 px-4 py-2 2xl:py-1">
            <Vue3EasyDataTable
    :headers="headers"
    :items="items"
  />
          </div>
        </div>
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import UAVCard from "../components/UAVCard.vue";
import Map from "../components/Map.vue";
import Vue3EasyDataTable from 'vue3-easy-data-table';
import 'vue3-easy-data-table/dist/style.css';
import { mapActions, mapGetters } from "vuex";
export default {
  components: {
    Vue3EasyDataTable,
    },
    data () {
      return {
        headers:[
          { text: "Name", value: "name" },
          { text: "Height (cm)", value: "height", sortable: true },
          { text: "Weight (kg)", value: "weight", sortable: true },
          { text: "Age", value: "age", sortable: true }
        ],
        items: [
          { "name": "Curry", "height": 178, "weight": 77, "age": 20 },
          { "name": "James", "height": 180, "weight": 75, "age": 21 },
          { "name": "Jordan", "height": 181, "weight": 73, "age": 22 }
        ],
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
