from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./status_page.db"  # Replace with your DB URL
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependency for DB sessions
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
      
Base.metadata.create_all(bind=engine)

# Initialize FastAPI app
app = FastAPI()

# Initialize WebSocket Manager with the app
socket_manager = create_socket_manager(app)

# Include API Routes
app.include_router(router)
