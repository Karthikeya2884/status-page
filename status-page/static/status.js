const socket = io("http://localhost:8000");

socket.on("status_update", (data) => {
    console.log(`Service ${data.service_id} updated to ${data.status}`);
});