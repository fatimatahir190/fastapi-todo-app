from fastapi import FastAPI
from database import Base, engine
import routers

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo App")

app.include_router(routers.router)