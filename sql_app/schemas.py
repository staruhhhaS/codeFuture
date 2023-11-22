#Пункт 3 в Задании 1

from pydantic import BaseModel

#стандартная форма для добавления
class StudentBase(BaseModel):
    name: str
    weight: float
    height: float
    age: int
    group: str

class StudentCreate(StudentBase):
    pass

class Student(BaseModel):

    id: int
    name: str
    weight: float
    height: float
    age: int
    group: str

    class Config:
        orm_mode = True


