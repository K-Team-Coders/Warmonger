import datetime

from pydantic import BaseModel

"""
Модель новостей для GET-POST запросов
"""
class New(BaseModel):
    id: int
    text: str
    datetime: datetime.datetime
    source: str

"""
Модель организаций для GET-POST запросов
"""
class Organisation(BaseModel):
    id: int
    name: str

"""
Модель личностей для GET-POST запросов
"""
class Persons(BaseModel):
    id: int
    name: str

"""
Модель тэгов для GET-POST запросов
"""
class Tags(BaseModel):
    id: int
    name: str

