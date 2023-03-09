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
        countries_list: ['Russia', 'USA']
      },
      getters: {
        allUAVs(state) {
            return state.UAV_list
        }
      },
      mutations: {
        
    
      },
      actions: {
        
      },
}