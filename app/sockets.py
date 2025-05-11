from fastapi_socketio import SocketManager

def create_socket_manager(app):
    return SocketManager(app=app)
