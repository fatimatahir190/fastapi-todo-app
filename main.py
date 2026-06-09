from fastapi import FastAPI
from database import Base, engine
from routers.todo import router

app = FastAPI(title="Todo App")

Base.metadata.create_all(bind=engine)

app.include_router(router)