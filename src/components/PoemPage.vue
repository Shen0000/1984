<template>
  <div class="main">
    <div class="poem">
      <h2 v-for="line in poem" v-bind:key="line.index">
        <br v-if="line=='\n'">
        {{line}}
      </h2>
    </div>
  </div>
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
h3 {
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
}
</style>
