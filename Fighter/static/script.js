const socket = io();

socket.on("new", function (data) {
    console.log(data)
    socket.emit("hello server", `Игрок с id: ${data} подключился`);
});