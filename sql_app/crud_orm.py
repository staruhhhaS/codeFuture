from sqlalchemy.orm import Session
from sql_app import models, schemas


def all_students(db: Session):
    students = db.query(models.Student).all()
    return {"data": students}


def create_student(student: schemas.StudentBase, db: Session):
    new_student = models.Student(**student.model_pump())
    db.add(new_student)
    db.commit()
    db.refresh(new_student)
    return {"message": "student created", "data": new_student}

def get_user_by_id(db:Session, student_id:int):
    return db.query(models.Student).filter(models.Student.id == student_id).first()

def put_user(db: Session, student_id: int, student_up: schemas.StudentBase):
    student = db.query(models.Student).filter(models.Student.id == student_id)

    if student.first() == None:
        return None

    student.update(student_up.dict(), synchronize_session=False)
    db.commit()

    return {"data" : "Обновлен"}

def delete_student(student_id:int, db: Session):
    student = db.query(models.Student).filter(models.Student.id == student_id)

    if student.first() == None:
        return None

    student.delete(synchronize_session=False)
    db.commit()

    return {"data" : "Успешно удален"}
