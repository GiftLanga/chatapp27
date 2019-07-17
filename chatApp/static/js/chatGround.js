$(function () {
  // Correctly decide between ws:// and wss://
  var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
  var ws_path = ws_scheme + '://' + window.location.host + "/chat/stream/";
  console.log("Connecting to " + ws_path);
  var socket = new ReconnectingWebSocket(ws_path);

  // Helpful debugging
  socket.onopen = function () {
      console.log("Connected to chat socket");
  };
  socket.onclose = function () {
      console.log("Disconnected from chat socket");
  }
})

// Says if we joined a room or not by if there's a div for it
inRoom = function (roomId) {
  return $("#room-" + roomId).length > 0;
};
// Room join/leave
$("li.room-link").click(function () {
  roomId = $(this).attr("data-room-id");
  if (inRoom(roomId)) {
      // Leave room
      $(this).removeClass("joined");
      socket.send(JSON.stringify({
          "command": "leave",  // determines which handler will be used (see chat/routing.py)
          "room": roomId
      }));
  } else {
      // Join room
      $(this).addClass("joined");
      socket.send(JSON.stringify({
          "command": "join",
          "room": roomId
      }));
  }
});