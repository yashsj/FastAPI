from fastapi import FastAPI, Depends
from typing import Annotated
from sqlalchemy.orm import Session

from TodoApp import models
from TodoApp.database import engine, SessionLocal
from TodoApp.models import Todo

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency=Annotated[Session,Depends(get_db)]

@app.get("/")
async def read_all(db: db_dependency):
    return db.query(Todo).all()
