<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <PoemPage msg="Welcome to Your Vue.js App"/>
</template>

<script>
import PoemPage from './components/PoemPage.vue'

export default {
  name: 'App',
  components: {
    PoemPage
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
