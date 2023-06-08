// Open a WebSocket connection
const socket = new WebSocket('ws://localhost:8000/ws/chat/notifications/');

// Connection opened
socket.addEventListener('open', (event) => {
    // Send a JSON message
    socket.send(JSON.stringify({ message: 'Hello, world!' }));
});

// Listen for messages
socket.addEventListener('message', (event) => {
    console.log('Message from server: ', JSON.parse(event.data));
});