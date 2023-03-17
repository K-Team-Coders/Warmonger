export default {
  state: {
    UAV_list: [
      {
        id: 0,
        name: "Orion",
        country: "Russia",
        company: "Artek",
        endurance: 6,
        range: 20000000,
        payload: 0,
        max_speed: 100,
      },
      {
        id: 1,
        name: "Haha",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 1000000,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 2,
        name: "Pizda",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 900,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      {
        id: 3,
        name: "Jora",
        country: "USA",
        company: "Antitac",
        endurance: 9,
        range: 7655,
        payload: 0,
        max_speed: 108,
      },
      
    ],
    countries_list: ["Все страны", "Russia", "USA"],
    choosed_country: " ",
    choosed_uav: '',
    choosed_range: 0,
  },
  mutations: {
    SET_ALLCOUNTRIES: (state, payload) => {
      state.countries_list = payload;
    },
    SET_ALLUAVS: (state, payload) => {
      state.UAV_list = payload;
    },
    change_current_UAV(state, choosed_uav){
      state.choosed_uav = choosed_uav
    },
    change_current_range(state, choosed_range){
      state.choosed_range = choosed_range
    }
  },
  getters: {
    allUAVS(state) {
      return state.UAV_list;
    },
    allCountries(state) {
      return state.countries_list;
    },
    uav_range(state){
      return state.choosed_range;
    }
    
    
    
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
    CHANGE_UAV (context, choosed_uav) {
      context.commit('change_current_UAV', choosed_uav);
      console.log(choosed_uav);
  },
  CHANGE_RANGE (context, choosed_range) {
    context.commit('change_current_range', choosed_range);
    console.log(choosed_range);
}
  }
};
