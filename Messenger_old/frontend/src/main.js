import { createApp } from 'vue'
import { Vue } from 'vue'
import NewTweet from './App.vue'
console.log("main.js vue подкючен")


const app = createApp({
    delimiters: ["[[", "]]"],
    el:"#tweets",
    data() {
      return { info:{} }
    },
    methods: {
        mounted1() {
            fetch("get_info_new_tweet/", {
                method: "GET",
                headers: {
                    "X-Requested-With": "XMLHttpRequest",
                }
            }).then(response => response.json()).then(data => {
                this.info = data['context']
                for (let i of data['context']){
                    console.log(i)
                    // this.info = i
                }
                console.log(this.info)
        });}
    },
    mounted() {
      fetch("get_info_new_tweet/", {
          method: "GET",
          headers: {
              "X-Requested-With": "XMLHttpRequest",
          }
      }).then(response => response.json()).then(data => {
          this.info = data['context']
          for (let i of data['context']){
              console.log(i)
              // this.info = i
          }
          console.log(this.info)
    });}
  })
  app.mounted1() 
  


Vue.component("NewTweet", NewTweet);

