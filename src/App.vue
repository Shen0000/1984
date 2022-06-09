<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <IntroSection/>
  <PoemPage id="poem"/>
</template>

<script>

import IntroSection from "./components/IntroSection.vue"
import PoemPage from './components/PoemPage.vue'

export default {
  name: 'App',
  components: {
    PoemPage,
    IntroSection
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
  /* margin-top: 60px; */
  display: flex;
  flex-direction: column;
  -ms-overflow-style: none;  /* IE and Edge */
  scrollbar-width: none;  /* Firefox */
  min-height: 100vh;
  /* overflow: visible; */
  /*the above is*/
  /* transition: all 1s; */
  /* max-width: 100%; */
  /* overflow-x: hidden; */
}

body::-webkit-scrollbar {
    display: none;
}

html {
    scroll-behavior: smooth;
}

</style>
