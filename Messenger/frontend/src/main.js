// new Vue({
//     delimiters: ["[[", "]]"],
//     el:"#tweets",
//     data: {
//             info: []
//     },
//     methods: {
//         mounted1() {
//         return axios
//           .get('/get_info_tweet/')
//           .then((response) => {this.info = response.data['context']; console.log(this.info)}).catch(error => console.log(error));
//
//         }
//
//         //
//         //     fetch("get_info_new_tweet/", {
//         //         method: "GET",
//         //         headers: {
//         //             "X-Requested-With": "XMLHttpRequest",
//         //         }
//         //     }).then(response => response.json()).then(data => {
//         //         this.info = data['context']
//         //         for (let i of data['context']){
//         //             console.log(i)
//         //             // this.info = i
//         //         }
//         //         console.log(this.info)
//         // });}
//     },
//     mounted() {
//         return axios
//           .get('/get_info_tweet/')
//           .then((response) => {this.info = response.data['context']; console.log(this.info)}).catch(error => console.log(error));
//
//     }
//     })
// // app.mounted1()
// // const vm = app
//
//
//
// Vue.component('Tweets', {
//     props: {
//         tweet_id: {
//             type:Number,
//             required: true
//         },
//         url_close_img: {
//             type: String,
//             // default: 100,
//             required: true
//         },
//         url_like_img: {
//             type: String,
//             // default: 100,
//             required: true
//         },
//         author_nickname: {
//             type:String,
//             required: true
//         },
//         text_tweet: {
//             type:String,
//             required: true
//         },
//         likes: {
//             type:Number,
//             required: true
//         }
//     },
//     data: function () {
//         return {
//             info2:1
//         }
//     },
//     methods: {
//       like_tweet_met(tweet_id) {
//           return axios
//           .get(`/home/${tweet_id}/like_tweet/`)
//           .then((response) => {this.info = response.data['context']; console.log(this.info); this.likes += 1}).catch(error => console.log(error));
//       }
//     },
//     template:
//     `
//         <div class="tweet">
//             <div class="logo">{{author_nickname[0]}}</div>
//                 <div id="tweet-content" class="tweet-content">
//                 <div class="tweet-actions-top">
//                     <a href="" class="tweet-author-nickname">{{author_nickname}}</a>
//                     <img :src="url_close_img" alt="" class="close-tweet">
//                 </div>
//                 <p class="tweet-text">{{text_tweet}}</p>
//                 <div class="tweet-actions-bottom">
//                     <img :src="url_like_img" alt="" @click="like_tweet_met(tweet_id)"><span class="tweet-likes" >{{likes}}</span>
//                 </div>
//             </div>
//         </div>
//     `
// })
