<template>
  <div
    class="items-center hover:bg-white transition mt-3 mb-2 text-sm w-[24rem] font-roboto rounded-lg bg-gray-300 bg-opacity-85"
  >
    <img
      class="rounded-t-lg shadow-md"
      src="../DJI_Phantom_4_in_Flight_March_2016.jpg"
      alt=""
    />
    <div
      class="flex transition flex-col justify-between p-2 ml-2 mr-4 leading-normal"
    >
      <p
        class="text-2xl my-2 font-monster font-bold tracking-tight text-gray-800"
      >
        {{ uav_name }}
      </p>
      <p class="mb-1 text-xl font-monster text-gray-800 border-b-2 border-black">
        Страна: <span class="font-bold"> {{ uav_country }} </span>
      </p>
      <p class="mb-1 text-lg font-monster font-normal text-black border-b-2 border-black">
        Компания: <span class="font-bold"> {{ uav_company }}</span>
      </p>
      <p class="mb-1 text-lg font-normal font-monster text-black border-b-2 border-black">
        Дальность, км: <span class="font-bold">  {{ uav_range / 1000 }} </span>
      </p>
      <p class="mb-1 text-lg font-normal text-black font-monster border-b-2 border-black">
        Нагрузка, кг:  <span class="font-bold">{{ uav_payload }}</span>
      </p>
      <p class="mb-1 text-lg font-normal text-black border-b-2 font-monster border-black">
        Макс.скорость, км/ч: <span class="font-bold"> {{ uav_max_speed }}</span>
      </p>
      <p class="text-lg font-normal text-black border-b-2 border-black font-monster">
        Время работы, ч: <span class="font-bold"> {{ uav_endurance }}</span>
      </p>
    </div>
    <a
        href="#"
        class="flex justify-center mt-2 hover:text-gray-50 items-center py-2 text-base font-medium text-center text-gray-50 bg-red-800 rounded-b-lg hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-300"
      >
        Узнать больше
        <svg
          aria-hidden="true"
          class="w-4 h-4 ml-2 -mr-1"
          fill="currentColor"
          viewBox="0 0 20 20"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            fill-rule="evenodd"
            d="M10.293 3.293a1 1 0 011.414 0l6 6a1 1 0 010 1.414l-6 6a1 1 0 01-1.414-1.414L14.586 11H3a1 1 0 110-2h11.586l-4.293-4.293a1 1 0 010-1.414z"
            clip-rule="evenodd"
          ></path>
        </svg>
      </a>
  </div>
</template>

<script>
export default {
  props: {
    uav_name: String,
    uav_country: String,
    uav_company: String,
    uav_endurance: Number,
    uav_range: Number,
    uav_payload: Number,
    uav_max_speed: Number,
  },
};
</script>

<style></style>
