#Пункт 1 в Задании 1

from sqlalchemy import Column, Integer, String, Float

#Механизм для взаимодействия с БД
from .database import Base

class Student(Base):
    #Название в бд (таблички)
    __tablename__ = "students"

    #задаем поля
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    weight = Column(Float, nullable=False)
    height = Column(Float, nullable=False)
    age = Column(Integer, nullable=False)
    group = Column(String, nullable=False)

