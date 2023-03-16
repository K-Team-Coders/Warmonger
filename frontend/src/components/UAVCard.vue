<template>
  
  <div
    class="flex justify-center  pb-2 items-center text-sm font-rale font-medium"
  >
    <div class="flex hover:bg-gray-700 flex-col justify-between p-3 leading-normal">
      <p class="text-lg font-bold tracking-tight text-white">
        {{uav_name}}
      </p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">Страна: {{uav_country}}</p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">Компания: {{uav_company}}</p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">
        Дальность, км: {{uav_range/1000}}
      </p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">
        Нагрузка, кг: {{uav_payload}}
      </p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">
        Макс.скорость, км/ч: {{uav_max_speed}}
      </p>
      <p class="mb-1 font-normal text-gray-200 border-b-2">
        Время работы, ч: {{uav_endurance}}
      </p>
    </div>
  </div>
</template>

<script>
export default {
    props: {
            uav_name: String,
            uav_country: String,
            uav_company: String,
            uav_endurance: Number,
            uav_range:  Number,
            uav_payload: Number,
            uav_max_speed: Number, 
        }
};
</script>

<style></style>
