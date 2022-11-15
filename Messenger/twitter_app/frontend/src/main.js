const app = new Vue({
    delimiters: ["[[", "]]"],
    el:"#tweets",
    data() {
      return { info:{} }
    },
    methods: {
        mounted1() {
           axios.get("get_info_new_tweet/")
            .then((response) => response.json().then((data) => this.info = response.data['context']))
            .catch(error => {
              this.errorMessage = error.message;
              console.error("There was an error!", error);
            });
           console.log(this.info )
            return true
        }
        //
        //     fetch("get_info_new_tweet/", {
        //         method: "GET",
        //         headers: {
        //             "X-Requested-With": "XMLHttpRequest",
        //         }
        //     }).then(response => response.json()).then(data => {
        //         this.info = data['context']
        //         for (let i of data['context']){
        //             console.log(i)
        //             // this.info = i
        //         }
        //         console.log(this.info)
        // });}
    },
    mounted() {
        axios.get("get_info_new_tweet/")
            .then((response) => response.json().then((data) => this.info = response.data['context']))
            .catch(error => {
                this.errorMessage = error.message;
                console.error("There was an error!", error);
            })
        console.log(this.info )
        return true
        //
        //   fetch("get_info_new_tweet/", {
        //       method: "GET",
        //       headers: {
        //           "X-Requested-With": "XMLHttpRequest",
        //       }
        //   }).then(response => response.json()).then(data => {
        //       this.info = data['context']
        //       for (let i of data['context']){
        //           console.log(i)
        //           // this.info = i
        //       }
        //       console.log(this.info)
        // });}
    }})
app.mounted1()
// const vm = app



Vue.component('Tweets', {
    props: {
        url_close_img: {
            type: String,
            // default: 100,
            required: true
        },
        url_like_img: {
            type: String,
            // default: 100,
            required: true
        },
        author_nickname: {
            type:String,
            required: true
        },
        text_tweet: {
            type:String,
            required: true
        },
        likes: {
            type:Number,
            required: true
        }
    },
    data: function () {
        return {
            info2:1
        }
    },

    template:
    `
        <div class="tweet">
            <div class="logo">{{author_nickname[0]}}</div>
                <div id="tweet-content" class="tweet-content">
                <div class="tweet-actions-top">
                    <a href="" class="tweet-author-nickname">{{author_nickname}}</a>
                    <img :src="url_close_img" alt="" class="close-tweet">
                </div>
                <p class="tweet-text">{{text_tweet}}</p>
                <div class="tweet-actions-bottom">
                    <img :src="url_like_img" alt=""><span class="tweet-likes">{{likes}}</span>
                </div>                         
            </div>
        </div>
    `
})
