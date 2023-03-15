export default {
  state: {
    UAV_list: [
      {
        id: 0,
        name: "Orion",
        country: "Russia",
        company: "Artek",
        endurance: 6,
        range: 50000,
        payload: 0,
        max_speed: 100,
      },
      {
        id: 1,
        name: "Haha",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 1000,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 1,
        name: "Haha",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 1000,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 1,
        name: "Haha",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 1000,
        payload: 0,
        max_speed: 108,
      },
    ],
    countries_list: ["Все страны", "Russia", "USA"],
    choosed_country: " ",
    choosed_uav: " ",
  },
  mutations: {
    SET_ALLCOUNTRIES: (state, payload) => {
      state.countries_list = payload;
    },
    SET_ALLUAVS: (state, payload) => {
      state.UAV_list = payload;
    },
  },
  getters: {
    allUAVS(state) {
      return state.UAV_list;
    },
    allCountries(state) {
      return state.countries_list;
    },
  },
  actions: {
    GET_ALLCOUNTRIES: async (context, payload) => {
      let countries_list = this.countries_list;
      context.commit("SET_ALLCOUNTRIES", countries_list);
    },
    GET_ALLUAVS: async (context, payload) => {
      let UAV_list= this.UAV_list;
      context.commit("SET_ALLUAVS", UAV_list);
    },
  }
};
