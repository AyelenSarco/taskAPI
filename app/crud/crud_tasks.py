from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from ..schemas import task_schema
from ..exceptions.exceptions import NotFoundException, InvalidInputException, DataBaseException
from ..models import task_model

def get_task(db: Session, task_id: int):
    db_task= db.query(task_model.Task).filter(task_model.Task.id == task_id).first()
    if not db_task:
        raise NotFoundException(f'Task with id {task_id} not found')
    return db_task


def create_task(db:Session, task: task_schema.TaskCreate, owner_id:int):
    if not task.title:
        raise InvalidInputException("Title is required")
    try:
        db_task = task_model.Task(title=task.title, description=task.description, owner_id=owner_id)
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
    except Exception as e:
        raise DataBaseException(str(e))
    return db_task

def update_task(db:Session, user_id:int, task: task_schema.Task):
    db_task = get_task(db,task.id)
    if not db_task.owner_id == user_id:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    try: 
        db_task.title = task.title
        db_task.description = task.description
        db_task.completed = task.completed
        db.commit()
        db.refresh(db_task)
    except Exception as e:
        raise DataBaseException(str(e))
    return db_task

def delete_task(db:Session, task_id: int, user_id:int):
    db_task = get_task(db,task_id)
    if not db_task.owner_id == user_id:
         raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized"
        )
    try:
        db.delete(db_task)
        db.commit()
    except Exception as e:
        raise DataBaseException(str(e))

def delete_tasks_from_user(db:Session, user_id:int):
    user_tasks = db.query(task_model.Task).filter(task_model.Task.owner_id==user_id).all()
    for task in user_tasks:
        delete_task(db=db, task_id=task.id, user_id=user_id)
    

def get_tasks_with_owner_id(db:Session, owner_id: int):
    return db.query(task_model.Task).filter(task_model.Task.owner_id==owner_id).all()