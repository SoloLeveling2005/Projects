let dates = new Date();
let date = dates.getDate()
let month = dates.getMonth() + 1
let year = dates.getFullYear()

if (date < 10) {
    date = `0${date}`
}
if (month < 10) {
    month = `0${month}`
} else if (month == 13) {
    month = 12
}
let today = `${date}.${month}.${year}`
// console.log(today);

document.getElementById('title_today').innerHTML = `Сегодня: ${today}`