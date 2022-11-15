


var element = document.querySelector(".left-menu");
var marginLeft = parseInt(getComputedStyle(element, true).marginLeft);
var marginRight = parseInt(getComputedStyle(element, true).marginRight);
document.querySelector(".main").style = `margin-left:${element.offsetWidth + marginLeft + marginRight - 50}px;`
document.querySelector(".top-menu").style = `margin-left:${element.offsetWidth + marginLeft + marginRight - 50}px;`
console.log(element.offsetWidth + marginLeft + marginRight - 50)
window.addEventListener('resize', function(event) {
    var element = document.querySelector(".left-menu");
    var marginLeft = parseInt(getComputedStyle(element, true).marginLeft);
    var marginRight = parseInt(getComputedStyle(element, true).marginRight);
    document.querySelector(".main").style = `margin-left:${element.offsetWidth + marginLeft + marginRight - 50}px;`
    document.querySelector(".top-menu").style = `margin-left:${element.offsetWidth + marginLeft + marginRight - 50}px;`
    console.log(element.offsetWidth + marginLeft + marginRight - 50)
}, true);


function randomIntFromInterval(min, max) { 
// min and max included
    return Math.floor(Math.random() * (max - min + 1) + min)
}


function new_tweet() {
    let tweet_text = document.querySelector(".tweet_text").value
    let tweet_id = String(+(new Date())).substr(6, 200) + randomIntFromInterval(100, 999)
    let author_id = getCookie('user_id')
    console.log(tweet_text)
    console.log(tweet_id)
    console.log(author_id)
    fetch("new_tweet/", {
        method: "POST",
        credentials: "same-origin",
        headers: {
          "X-Requested-With": "XMLHttpRequest",
          "X-CSRFToken": getCookie("csrftoken"),
        },
        body: JSON.stringify({id_tweet: tweet_id,author_id:author_id,tweet_text:tweet_text})
      })
      .then(response => response.json())
      .then(data => {
        
    });
    console.log("Запрос прошел успешно");
    document.querySelector(".tweet_text").value = ""
}



