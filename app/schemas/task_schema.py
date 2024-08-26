from typing import Union
from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: Union [str, None] = None


class TaskCreate(TaskBase):
    completed: Union[bool, None] = None 


class TaskUpdate(TaskCreate):
    id:int

class Task(TaskUpdate):
    owner_id: int 

    class Config:
        from_attributes = True

# Pydantic's orm_mode will tell the Pydantic model to read the data even if it is not a dict, but an ORM model (or any other arbitrary object with attributes).

