import axios from 'axios'
export default {
  state: {
    UAV_list: [
      
    ],
    countries_list: ["Все страны", "Russia", "USA"],
    choosed_country: " ",
    choosed_uav: "",
    choosed_range: 0,
    choosed_icon: '',
  },
  mutations: {
    SET_ALLCOUNTRIES: (state, payload) => {
      state.countries_list = payload;
    },
    SET_ALLUAVS: (state, payload) => {
      state.UAV_list = payload;
    },
    change_current_UAV(state, choosed_uav) {
      state.choosed_uav = choosed_uav;
    },
    change_current_range(state, choosed_range) {
      state.choosed_range = choosed_range;
    },
    change_current_icon(state, icon) {
      state.choosed_icon =icon;
    },
  },
  getters: {
    allUAVS(state) {
      return state.UAV_list;
    },
    allCountries(state) {
      return state.countries_list;
    },
    uav_range(state) {
      return state.choosed_range;
    },
    uav_icon(state) {
      return state.choosed_icon;
    },
  },
  actions: {
    GET_ALLCOUNTRIES: async (context, payload) => {
      let countries_list = this.countries_list;
      context.commit("SET_ALLCOUNTRIES", countries_list);
    },
    GET_ALLUAVS: async (context, payload) => {
      let UAV_list = await axios.get('http://192.168.0.156:8081/getDronesCnas/');
      context.commit("SET_ALLUAVS", UAV_list.data);
    },
    CHANGE_UAV(context, choosed_uav) {
      context.commit("change_current_UAV", choosed_uav);
      console.log(choosed_uav);
    },
    CHANGE_RANGE(context, choosed_range) {
      context.commit("change_current_range", choosed_range);
      console.log(choosed_range);
    },
    CHANGE_ICON(context, choosed_icon) {
      context.commit("change_current_icon", choosed_icon);
      console.log(choosed_icon);
    },
  },
};
