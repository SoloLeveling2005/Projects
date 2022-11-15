console.log("Есть контакт")


document.querySelector(".look_auth_block").addEventListener("click", function() {
    document.querySelector(".authorization").style = "display:block;"
    document.querySelector(".login").style = "display:none;"
});

document.querySelector(".look_log_block").addEventListener("click", function() {
    document.querySelector(".login").style = "display:block;"
    document.querySelector(".authorization").style = "display:none;"
});

look_error()
function look_error(){
    if (data != undefined) {
        document.querySelector(".error").style = "display:flex;"
        console.log(data)
        document.querySelector(".error").innerHTML = data['error']
    }

    setTimeout(function(){
        document.querySelector(".error").style = "display:none;"
    },3000)
}
