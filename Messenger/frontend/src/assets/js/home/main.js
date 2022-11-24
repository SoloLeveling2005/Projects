

// Контроль размер меню и main блока
let element = document.querySelector(".left-menu");
document.querySelector(".main").style = `margin-left:${element.offsetWidth}px;`
window.addEventListener('resize', function(event) {
    let element = document.querySelector(".left-menu");
    document.querySelector(".main").style = `margin-left:${element.offsetWidth}px;`
}, true);



let element_1 = document.querySelector(".left-menu");
let element_2 = document.querySelector(".main");
document.querySelector(".right-menu").style = `margin-left:${element_1.offsetWidth + element_2.offsetWidth}px;`

window.addEventListener('resize', function(event) {
    let element_1 = document.querySelector(".left-menu");
    let element_2 = document.querySelector(".main");
    document.querySelector(".right-menu").style = `margin-left:${element_1.offsetWidth + element_2.offsetWidth}px;`
}, true);

// function randomIntFromInterval(min, max) {
// // min and max included
//     return Math.floor(Math.random() * (max - min + 1) + min)
// }


// function new_tweet() {
//     let tweet_text = document.querySelector(".tweet_text").value
//     let tweet_id = String(+(new Date())).substr(6, 200) + randomIntFromInterval(100, 999)
//     let author_id = getCookie('user_id')
//     console.log(tweet_text)
//     console.log(tweet_id)
//     console.log(author_id)
//     fetch("new_tweet/", {
//         method: "POST",
//         credentials: "same-origin",
//         headers: {
//           "X-Requested-With": "XMLHttpRequest",
//           "X-CSRFToken": getCookie("csrftoken"),
//         },
//         body: JSON.stringify({id_tweet: tweet_id,author_id:author_id,tweet_text:tweet_text})
//       })
//       // .then(response => response.json())
//       // .then(data => {
//       //
//     // });
//     console.log("Запрос прошел успешно");
//     document.querySelector(".tweet_text").value = ""
// }
//
