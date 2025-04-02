<template>
  <div class="hello">
    <h1>Météo de {{ city }}</h1>
    <!-- <h1>{{ msg }}</h1> -->

    <img :src="require('@/assets/refreshLogo.svg')" class="logo-image" @click="fetchData(true)"/>



    <div class="hourly-list-wrapper">
      <h2 class="hourly-list-header"> Prévisions par heure</h2>
      <div class="hourly-list">
          <div v-for="hour in dataHourly" :key="hour.time" class="hour-item">
            <div v-if="currentEpoch-3600 <= hour.time_epoch ">
              <span class="hour">{{ hour.time.split(" ")[1] }}</span>
              <img :src="hour.condition.icon" alt="weather icon" />
              <span class="temp">{{ hour.temp_c }}°C</span>
            </div>
          </div>
      </div>
    </div>

    <div class="hourly-list-wrapper">
      <h2 class="hourly-list-header"> Prévisions par jour</h2>
      <div class="daily-list">

          <div v-for="day in dataDaily" :key="day.day" class="daily-item">
            <div class="daily-date">
              <span class="hour">{{ getDay(day.date) }}</span>
              <span class="hour">{{new Date(day.date).toLocaleDateString('fr-FR')}}</span>
            </div>
            <span class="temp">{{ day.day.avgtemp_c }}°C</span>
            <img :src="day.day.condition.icon" alt="weather icon" />
          </div>
          
      </div>
    </div>




  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HelloWorld',
  props: {
    city: {
      type: String,
      required: true
    }
  },
  data() {
    return {
      dataHourly: [],
      dataDaily: [],
      day: {},
      currentEpoch: Math.floor(Date.now() / 1000),
    };
  },
  methods: {
    getDay(dateStr){
      const date = new Date(dateStr);

      const daysOfWeek = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"];

      if(date.setHours(0,0,0,0) == new Date().setHours(0,0,0,0)){
        return "Aujourd'hui"
      }
      return daysOfWeek[date.getDay()];
    },
    fetchData(refresh=false) {
        axios
          .get('http://localhost:8000/api/forecast', {
          params: {
            arg: "Paris",
            refresh: refresh
          }
         })
          .then((response) => {
            this.dataDaily=response.data.forecast.forecastday
            this.dataHourly=response.data.forecast.forecastday[0].hour
          })
          .catch((error) => {
              console.error(error)
          })
    },
  },
  mounted() {
    this.fetchData()
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hourly-forecast {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.forecast-container {
  display: flex;
  overflow-x: auto;
  width: 100%;
}

button {
  margin-top: 10px;
}

.hourly-list-wrapper {
  width: 100%;
  padding: 20px;
}

.hourly-list {
  display: flex;
  justify-content: center;
  align-items: center;
  list-style-type: none;
  padding: 0;

}

.hour-item {
  display: flex;
  flex-direction: column;
  align-items: center; 
}

.hour {
  display: block;
  font-weight: 700;
}

.temp {
  display: block;
  font-size: 16px;
  font-weight: 700;
}
.daily-date {
  display: flex;
  flex-direction: column;
  align-items: center; 
}

.daily-item{
  display: flex;
  flex-direction: row;
  align-items: center; 
  justify-content: space-around;

  
}

.logo-image {
  max-width: 30px;
  height: auto;
  cursor: pointer;
}
</style>
