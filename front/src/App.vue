<template>
  <img alt="Vue logo" src="./assets/weather.png" style="max-width: 200px;height: auto;">
  <WeatherForecast :city="cityName"/>
</template>

<script>
import WeatherForecast from './components/WeatherForecast.vue'

export default {
  name: 'App',
  components: {
    WeatherForecast
  },
  data() {
    return {
      cityName: "Paris"
    }
  }

}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
