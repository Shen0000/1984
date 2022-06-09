<template>
  <header class="main">
    <div class="background-image"></div>
    <div class="poem">
      <h1 class="title"><strong>1984</strong></h1>
      <br>
      <h2 class="author"><strong>By: Brendan Shen</strong></h2>
      <br><br>
      <h2 v-for="line in poem" v-bind:key="line.index">
        <br v-if="line=='\n'">
        {{line}}
      </h2>
    </div>
  </header>
</template>

<script>
import PoemJSON from "../json/poem.json"

export default {
  name: 'PoemPage',
  props: {
    msg: String
  },
  data() {
      return {
          poem: PoemJSON
      }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

/* h3 {
  margin: 40px 0 0;
}


ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
} */

.main {
  margin: 10vh;
  padding-top: 5vh;
}

.main .background-image{
  /* background: rgb(0, 0, 0); */
  z-index: -1;
  position: absolute;
  left: 0;
  top: 0;
  width: 100%;
  height: 1000%;
  background: url(http://www.wakingtimes.com/wp-content/uploads/2014/08/big-brother-spy-eye-surveillance.png);
  background-size: cover;
  background-attachment: fixed;
  background-position: center;
  background-repeat: no-repeat;
  filter: blur(4px);
  -webkit-filter: blur(4px);
}

.poem {
  font-size: 1rem;
  font-family: "Montserrat";
  line-height: 1.2em;
  font-weight: 400;
  /* font-style: italic; */
  letter-spacing: 3px;
  color: #ffd0d0;
  margin-bottom: 5px;
  width: 65%;
  margin: 0 auto;
  padding: 20px;
  border: 2px solid#010314;
  border-radius: 25px;
  /* text-transform: lowercase; */
  background-color: rgb(0,0,0); /* Fallback color */
  background-color: rgba(0,0,0, 0.4); /* Black w/opacity/see-through */
}

.title {
  font-size: 4rem;
  color: rgb(7, 0, 63);
  text-shadow:
    -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000,
    4px 4px 5px red;
}

.author {
  font-size: 2.2rem;
  color: rgb(7, 0, 63);
  text-shadow:
    /* -1px -1px 0 #000,
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000, */
    3px 3px 4px red;
}

</style>
