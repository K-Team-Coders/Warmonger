<template>
  <div
    class="hover:bg-white transition mt-3 mb-2 text-sm w-[24rem] font-roboto rounded-lg bg-gray-300 bg-opacity-85"
  >
    <img
      class="rounded-t-lg shadow-md h-[20rem] w-full"
      :src="uav_img"
      alt=""
    />
    <div
      class="p-2 mr-4"
    >
      <p
        class="text-4xl my-2 font-mono font-bold tracking-tight text-gray-800"
      >
        {{ uav_name }}
      </p>
      <p
        class="mb-1 text-xl font-monster text-gray-800 border-b-2 border-black"
      >
        Страна: <span class="font-bold"> {{ uav_country }} </span>
      </p>
      <p
        class="mb-1 h-8 text-lg font-monster font-normal text-black border-b-2 border-black"
      >
        Компания: <span class="font-bold text-sm "> {{ uav_company }}</span>
      </p>
      <p
        class="mb-1 text-lg font-normal font-monster text-black border-b-2 border-black"
      >
        Дальность, км: <span class="font-bold"> {{ uav_range / 1000 }} </span>
      </p>
      <p
        class="mb-1 text-lg font-normal text-black font-monster border-b-2 border-black"
      >
        Нагрузка, кг: <span class="font-bold">{{ uav_payload }}</span>
      </p>
      <p
        class="mb-1 text-lg font-normal text-black border-b-2 font-monster border-black"
      >
        Макс.скорость, км/ч: <span class="font-bold"> {{ uav_max_speed }}</span>
      </p>
      <p
        class="text-lg font-normal text-black border-b-2 border-black font-monster"
      >
        Время работы, ч: <span class="font-bold"> {{ uav_endurance }}</span>
      </p>
    </div>
    <button
      @click="isModalOpen = true"
      class=" flex mt-3 justify-center w-full hover:text-gray-50 py-2 text-base font-monster font-medium text-center text-gray-50 bg-red-800 rounded-b-lg hover:bg-red-900 focus:ring-4 focus:outline-none focus:ring-red-300"
    >
      <a href="#" class="hover:text-gray-50 flex items-center text-lg">
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
    </button>
    <div>
      <ModalWindow
        v-if="isModalOpen"
        :uav_href="uav_img"
        :uav_company="uav_company"
        :uav_country="uav_country"
        :uav_endurance="uav_endurance"
        :uav_max_speed="uav_max_speed"
        :uav_name="uav_name"
        :uav_payload="uav_payload"
        :uav_range="uav_range"
        @close="isModalOpen = false"
      />
    </div>
  </div>
</template>

<script>
import ModalWindow from "./ModalWindow.vue";
export default {
  components: {
    ModalWindow,
  },
  data() {
    return {
      isModalOpen: false,
    };
  },
  emits: ["close"],

  props: {
    uav_img: String,
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
