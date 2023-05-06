<template>
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
</template>

<script>
export default {
    name: 'NewTweet',
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
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.tweet {
    display: flex;
}
.tweet .logo {
    width: 50px;
    min-width: 50px;
    min-height: 50px;
    height: 50px;
    font-size: 24px;
    color: white;
    background-color: #455a64;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 0;
    border-radius: 90px;
    margin-right: 10px;
} 
.tweet .logo:hover {
    cursor: pointer;
    -webkit-filter: brightness(70%);
    -webkit-transition: all .5s ease;
    -moz-transition: all .5s ease;
    -o-transition: all .5s ease;
    -ms-transition: all .5s ease;
    transition: all .5s ease;
}
.tweet-content .tweet-actions-top img {
    margin-right: 10px;
    /* margin-top: 2px; */
    float: right;
}
.tweet-content .tweet-actions-top img:hover {
    background-color: #e1eef6;
    cursor: pointer;
}
.tweet-content .tweet-actions-top .close-tweet {
    padding: 5px;
    border: 0;
    border-radius: 90px;
    width: 18px;
    height: 18px;
    float: right;
}
.tweet-content .tweet-text {
    margin-top: 7px;
}
.tweet-content .tweet-actions-top .tweet-author-nickname {
    color: black;
    text-decoration: none;
}
.tweet-content .tweet-actions-top .tweet-author-nickname:hover {
    text-decoration: underline;
}
.tweet-content .tweet-actions-bottom {
    display: flex;
    align-items: center;
    margin-top: 10px;
}
/*.tweet-content .tweet-actions-bottom img {
     padding: 5px;
    border: 0px;
    border-radius: 60px; 
}*/
.tweet-content .tweet-actions-bottom img:hover {
    cursor: pointer;
    /* background-color: #e1eef6; */
}
.tweet-content .tweet-actions-bottom .tweet-likes {
    font-size: 14px;
    margin-left:5px ;
}
</style>