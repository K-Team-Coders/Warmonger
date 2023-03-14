export default{
    state: {
        
        UAV_list: [ {
            id: 0,
            name: 'Orion',
            country: 'Russia',
            company: 'Artek',
            endurance: 6,
            range:  50000,
            payload: 0,
            max_speed: 100,
            coords: [34,67]
          },
          {
            id: 1,
            name: 'Haha',
            country: 'USA',
            company: 'Antitac',
            endurance: 9,
            range:  1000,
            payload: 0,
            max_speed: 108,
            coords: [55,88]
          }
        ],
        countries_list: ['Все страны', 'Russia', 'USA'],
        choosed_country: ' ',
        choosed_uav: ' ',

      },
      getters: {
        allUAVs(state) {
          return state.UAV_list
        },
        allCountries(state) {
          return state.countries_list
        },
      },
      actions: {
        GET_ALLCOUNTRIES: async (context) => {
          let {countries_list} = this.countries_list;
          context.commit('SET_ALLCOUNTRIES', countries_list)
        },
          
      },
      mutations: {
          SET_ALLCOUNTRIES: (state, payload) => {
            state.countries_list = payload;
          },
    
      },
      
      }