from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from contextlib import contextmanager

# Load environment variables
load_dotenv()

app = FastAPI(title="Test Fullstack API")

# CORS setup
origins = os.getenv("ALLOWED_ORIGINS", "*").split(",")
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database setup
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Models
class Todo(Base):
    __tablename__ = "todos"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    completed = Column(Boolean, default=False)

# Create tables
Base.metadata.create_all(bind=engine)

# Pydantic models
class TodoCreate(BaseModel):
    title: str
    completed: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    completed: bool

# Database dependency
@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/")
def root():
    return {"message": "Test Fullstack API is running!"}

@app.get("/api/hello")
def hello():
    return {"message": "Hello from the backend! 👋"}

@app.get("/api/todos", response_model=List[TodoResponse])
def get_todos():
    with get_db() as db:
        todos = db.query(Todo).all()
        return todos

@app.post("/api/todos", response_model=TodoResponse)
def create_todo(todo: TodoCreate):
    with get_db() as db:
        db_todo = Todo(title=todo.title, completed=todo.completed)
        db.add(db_todo)
        db.commit()
        db.refresh(db_todo)
        return db_todo

@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "database": "connected" if DATABASE_URL else "not configured",
        "environment": os.getenv("ENV", "development")
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8001))  # 8001로 변경
    uvicorn.run(app, host="0.0.0.0", port=port)