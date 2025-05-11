from fastapi import FastAPI
from app.database import Base, engine
from app.sockets import socket_manager
from app.routes import router

# Initialize database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Include WebSocket Manager
socket_manager.init_app(app)

# Include API Routes
app.include_router(router)