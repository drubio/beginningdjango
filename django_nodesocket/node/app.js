var app = require('express')();
var server = require('http').Server(app);
var io = require('socket.io')(server);

server.listen(3000);

io.on('connection', function (socket) {
  console.log("Client just connected to node.js");
  socket.emit('dailyspecials', { message: 'You just connected to the daily specials channel, one second while we get the specials!' });
  socket.on('admindailyspecials', function (data) {
      console.log("Client just sent admindailyspecials data!");
      socket.broadcast.emit('dailyspecials', { message: data});
  });
});