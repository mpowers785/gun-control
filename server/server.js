const express = require('express');
const app = express();
const socket = require('socket.io');

app.use(express.static('public'));

let server = app.listen(3000, console.log('Listening on 3000'));
let io = socket(server);

io.sockets.on('connection', socket => {
    console.log(`new user: ${socket.id}`);

    socket.on('breakPressed', data => {
        console.log('break');
        socket.broadcast.emit('buttonPressed', data);
    });

    socket.on('notBreak', data => {
        socket.broadcast.emit('notPressed', data);
    });

    socket.on('placePressed', data => {
        console.log('placed');
        socket.broadcast.emit('placePressed', data);
    });

    socket.on('notPlace', data => {
        socket.broadcast.emit('notPlace', data);
    });
});