import uvicorn

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from sql_app import schemas, models, crud_orm

from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/student/")
def create_student(student : schemas.StudentBase, db: Session = Depends(get_db)):
    return crud_orm.create_student(student, db)


if __name__ == "__main__":
    uvicorn.run(app, port=8001)