<template>
  <div id="app">
    <VapiComponent />
  </div>
</template>

<script>
import VapiComponent from './components/VapiComponent.vue';

export default {
  name: 'App',
  components: {
    VapiComponent
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
