const express = require("express");
const http = require("http");
const path = require("path");
const socketIO = require("socket.io");

const app = express();
const server = http.Server(app);
const io = socketIO(server);


app.set("port", 5000)
app.use("/static", express.static(__dirname + "/static"));

app.get("/", function (request, response) {
    response.sendFile(path.join(__dirname + "/static", "index.html"));
});

server.listen(5000, function () {
    console.log("Starting server on port 5000")
})

io.on("connection", function (socket) {
    socket.emit("new",socket.id)
    socket.on("hello server", function (data) {
        console.log(data);
    });

});