<template>
  <!-- <img alt="Vue logo" src="./assets/logo.png"> -->
  <IntroSection/>
  <PoemPage id="poem"/>
  <footer>
    <h1>Check out the code!</h1>
    <ul class="social-list">  
        <li class="social-list__item">
          <a class="social-list__link" href="https://github.com/Shen0000/1984" target="_blank"><i class="fab fa-github" aria-hidden="true"></i></a>
        </li>
    </ul>
  </footer>
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
  font-family: 'Montserrat';
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
  /* overflow: hidden; */
}

body::-webkit-scrollbar {
    display: none;
}

html {
    scroll-behavior: smooth;
}

footer {
	background: linear-gradient(rgb(71, 71, 71), rgb(255, 255, 255));
  /* padding: 3vw; */
  padding-top: 2vh;
  padding-bottom: 2vh;
  /* border: 1px solid black; */
  height: 15%;
  width: 102%;
  /* transition: all 2s; */
  transform: translate(-1vw, 0);
}
.footer-text {
	font-size: 50px;
	color: #272525;
}

.logo:hover {
	opacity: 0.8;
	transform: scale(1.1);
}
.social-list__link:focus,
.social-list__link:hover {
	opacity: .8;
	outline: none;
}
.social-list__item:hover {
	transform: scale(1.1);
}
.social-list {
	list-style: none;
	display: flex;
	justify-content: center;
	margin: 2em 0;
	padding: 0;
}
.social-list__item {
	transition: transform 250ms ease-in-out;
	margin: 0 .5em;
}
.social-list__link {
	font-size: 40px;
	color: var(--social);
	padding: .5em;
    transition: color 2s;
}

</style>
