<template>
  <body class="bg-idealblack">
    <Header2></Header2>
    <div class="p-6">
      <div class="">
        <div class="sm:hidden">
          <label for="tabs" class="sr-only">Select</label>
          <select
            id="tabs"
            class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5"
          >
            <option>MetaSpider</option>
            <option>Spider</option>
          </select>
        </div>
        <ul
          class="hidden text-lg font-medium text-center text-gray-500 divide-x divide-gray-300 rounded-lg shadow sm:flex w-1/5"
        >
          <li class="w-full">
            <a
              href="#"
              class="inline-block w-full p-2 text-gray-900 bg-gray-200 hover:text-gray-700 rounded-l-lg focus:ring-4 focus:ring-blue-300 active focus:outline-none "
              aria-current="page"
              >MetaSpider</a
            >
          </li>
          <li class="w-full">
            <a
              href="#"
              class="inline-block w-full p-2 bg-white hover:text-gray-700 rounded-r-lg hover:bg-gray-900 focus:ring-4 focus:ring-blue-300 focus:outline-none"
              >Spider</a
            >
          </li>
        </ul>
      </div>
      <div class="mt-2">
        <Vue3EasyDataTable
        table-class-name="customize-table"
        :headers="headers"
        :items="items"
      />
      </div>
    </div>
    <Footer></Footer>
  </body>
</template>

<script>
import Vue3EasyDataTable from "vue3-easy-data-table";
import Header2 from "@/components/Header2.vue";
import "vue3-easy-data-table/dist/style.css";
export default {
  components: {
    Vue3EasyDataTable,
    Header2,
  },
  data() {
    return {
      headers: [
        { text: "Name", value: "name" },
        { text: "Height (cm)", value: "height", sortable: true },
        { text: "Age", value: "age", sortable: true },
      ],
      items: [
        { name: "Curry", height: 178, weight: 77, age: 20 },
        { name: "James", height: 180, weight: 75, age: 21 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
        { name: "Jordan", height: 181, weight: 73, age: 22 },
      ],
    };
  },
};
</script>

<style>
.ymap-container {
  width: 100%;
  height: 100vh;
}
.customize-table {
  --easy-table-border: 2px solid #343537;
  --easy-table-row-border: 1px solid #6d5211;

  --easy-table-header-font-size: 16px;
  --easy-table-header-height: 70px;
  --easy-table-header-font-color: #e0d9d9;
  --easy-table-header-background-color: #791414;

  --easy-table-header-item-padding: 10px 15px;

  --easy-table-body-even-row-font-color: #fff;
  --easy-table-body-even-row-background-color: #82898f;

  --easy-table-body-row-font-color: #c0c7d2;
  --easy-table-body-row-background-color: #343537;
  --easy-table-body-row-height: 50px;
  --easy-table-body-row-font-size: 20px;

  --easy-table-body-row-hover-font-color: #2d3a4f;
  --easy-table-body-row-hover-background-color: #eee;

  --easy-table-body-item-padding: 10px 15px;

  --easy-table-footer-background-color: #494a4c;
  --easy-table-footer-font-color: #c0c7d2;
  --easy-table-footer-font-size: 20px;
  --easy-table-footer-padding: 0px 10px;
  --easy-table-footer-height: 50px;

  --easy-table-rows-per-page-selector-width: 70px;
  --easy-table-rows-per-page-selector-option-padding: 10px;
  --easy-table-rows-per-page-selector-z-index: 1;

  --easy-table-scrollbar-track-color: #2d3a4f;
  --easy-table-scrollbar-color: #5e3636;
  --easy-table-scrollbar-thumb-color: #4c5d7a;
  --easy-table-scrollbar-corner-color: #2d3a4f;

  --easy-table-loading-mask-background-color: #4f2d2d;
}
</style>
