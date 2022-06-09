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

@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@100&family=Square+Peg&family=Yantramanav:wght@300&display=swap');

#app {
  font-family: garamond;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  display: flex;
  flex-direction: column;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
  min-height: 100vh;
  /*the above is*/
}

body::-webkit-scrollbar {
    display: none;
}

</style>
