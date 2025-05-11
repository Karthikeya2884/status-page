from fastapi import FastAPI
from app.database import Base, engine
from app.sockets import create_socket_manager
from app.routes import router

# Initialize database
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Initialize WebSocket Manager with the app
socket_manager = create_socket_manager(app)

# Include API Routes
app.include_router(router)
