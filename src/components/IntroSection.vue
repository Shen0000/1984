<template>
  <div class="intro">
    <h1><strong>Welcome!</strong></h1>
    <br><br><br><br><br><br>
    <h2>
        After reading 1984, I was heavily inspired by the themes and ideas brought forth by George Orwell.
    </h2>
    <h2>
        As a result, I decided to write a poem drawing from the events that transpired in Airstrip One.
    </h2>
    <h2>
        The goal of this poem is to capture the feeling I got during and after reading 1984, and to transport 
    </h2>
    <h2>
        the reader into this dystopian world so they can better understand the horrors of such a society.
    </h2>
    <br><br><br><br><br><br>
    <button class="scroll-button" onclick="window.location.href='/#poem'"><span>Read Poem</span></button>
  </div>
</template>

<script>
export default {
  name: 'IntroSection',
  props: {
    msg: String
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

.intro {
    font-family: "Montserrat";
    background: linear-gradient(rgb(255, 255, 255), rgb(132, 132, 132));
    height: auto;
    width: calc(97vw);
    height: 105vh;
    /* border: 2px solid#010314; */
    /* border-radius: 15px;   */
    transform: translate(-7px, -10px);
    /* position: absolute; */
    padding: 20px;
}

.scroll-button {
  font-family: 'Montserrat', sans-serif;
  display: inline-block;
  border-radius: 4px;
  background-color: #1d1d1d;
  border: none;
  color: #ffffff;
  text-align: center;
  font-size: 18px;
  padding: 20px;
  width: 210px;
  transition: all 0.5s;
  cursor: pointer;
  margin: 5px;
}

.scroll-button span {
  cursor: pointer;
  display: inline-block;
  position: relative;
  transition: 0.5s;
}
.scroll-button span:after {
  content: "\00bb";
  position: absolute;
  opacity: 0;
  top: 0;
  right: -20px;
  transition: 0.5s;
}
.scroll-button:hover span {
  padding-right: 25px;
}
.scroll-button:hover span:after {
  opacity: 1;
  right: 0;
}

</style>
