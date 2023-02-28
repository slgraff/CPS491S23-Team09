// Connect to the server
const socket = io();

// Event listener for the up button
document.getElementById("up").addEventListener("click", function() {
  // Add  code here to send the "up" command to the iRobot
  socket.emit("move", "up");
});

// Event listener for the down button
document.getElementById("down").addEventListener("click", function() {
  // Add  code here to send the "down" command to the iRobot
  socket.emit("move", "down");
});

// Event listener for the left button
document.getElementById("left").addEventListener("click", function() {
  // Add  code here to send the "left" command to the iRobot
  socket.emit("move", "left");
});

// Event listener for the right button
document.getElementById("right").addEventListener("click", function() {
  // Add  code here to send the "right" command to the iRobot
  socket.emit("move", "right");
});

 // Event listener for the stop button
document.getElementById("stop").addEventListener("click", function() {
  // Add  code here to send the "right" command to the iRobot  
  socket.emit("move", "stop");
});
