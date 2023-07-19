console.log("hi")
const searchText = document.getElementById('APjFqb').textContent
let searchAnswer = ""
console.log(searchText)

let templateCode = `
    <div id="searchBlock" style="margin:0 50px; padding:20px; border:1px solid white; min-height:500px; height:max-content; width:22%; font-size:16px; font-family: Söhne,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,Helvetica Neue,Arial,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;">
        <div style="" id="searchAnswer">
            Начинаю поиск 🙂
        </div>
    </div>
`

if (!document.querySelector('#rhs')) {
    document.querySelector('.GyAeWb').innerHTML += templateCode;
} else {
    document.querySelector('#rhs').innerHTML += templateCode;
    document.querySelector('#searchBlock').style = `
        padding:20px; border:1px solid white; min-height:500px; height:max-content; width:90%; font-size:16px; font-family: Söhne,ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Ubuntu,Cantarell,Noto Sans,sans-serif,Helvetica Neue,Arial,Apple Color Emoji,Segoe UI Emoji,Segoe UI Symbol,Noto Color Emoji;
    `
}


const url = 'https://free.churchless.tech/v1/chat/completions';
const headers = { 'Content-Type': 'application/json' };
const data = {
  model: 'gpt-3.5-turbo',
  messages: [{ role: 'user', content: searchText }]
};

fetch(url, {
  method: 'POST',
  headers,
  body: JSON.stringify(data)
})
.then(response => {
if (!response.ok) {
    throw new Error('Network response was not ok');
}
return response.json();
})
.then(data => {
    document.querySelector('#searchAnswer').innerHTML = ""
    searchAnswer = data['choices'][0]['message']['content'];
    let delayPerCharacter = 50; // Задержка в миллисекундах между каждым символом
    console.log(data)
    function newWord(word) {
        document.querySelector('#searchAnswer').innerHTML += word
    }
    for (let i in searchAnswer) {
        setTimeout(() => {
            newWord(searchAnswer[i])
        }, delayPerCharacter * i)
    }   

})
.catch(error => {
    console.error('Ошибка при выполнении запроса:', error.message);
});



