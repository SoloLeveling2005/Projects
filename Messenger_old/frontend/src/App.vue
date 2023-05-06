<!-- <template>
  <img alt="Vue logo" src="./assets/logo.png">
  <NewTweet msg="Welcome to Your Vue.js App"/>
</template> -->

<script>
import NewTweet from './components/home/tweet.vue'

export default {
    name: 'NewTweet',
    components: {
      NewTweet
    }
}
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
