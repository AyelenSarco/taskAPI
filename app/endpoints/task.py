from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import Annotated
from ..schemas import task_schema,user_schema
from ..deps import get_db,get_current_active_user
from ..crud import crud_tasks


router = APIRouter()    



@router.get("/tasks/user_tasks", response_model=list[task_schema.TaskCreate])
async def tasks_from_user(
    current_user: Annotated [user_schema.User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    
    return crud_tasks.get_tasks_with_owner_id(db=db, owner_id=current_user.id)

@router.delete("/tasks/delete_task_user")
async def delete_tasks_from_user(
    current_user: Annotated [user_schema.User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
):
    crud_tasks.delete_tasks_from_user(db=db, user_id=current_user.id)

@router.post("/task", response_model = task_schema.TaskCreate)
def create_task(
    task: task_schema.TaskCreate, 
    current_user: Annotated [user_schema.User, Depends(get_current_active_user)],
    db: Session = Depends(get_db)
    
):
    return crud_tasks.create_task(db=db, task = task, owner_id = current_user.id)



@router.post("/tasks/update", response_model = task_schema.Task)
def update_task( 
    current_user: Annotated [user_schema.User, Depends(get_current_active_user)],
    task:task_schema.TaskUpdate, 
    db:Session = Depends(get_db),
):  
    return crud_tasks.update_task(db=db, 
                            user_id=current_user.id, 
                            task=task)



@router.delete("/tasks/{task_id}", response_model=None)
def delete_task(
    current_user: Annotated [user_schema.User, Depends(get_current_active_user)],
    task_id: int, 
    db: Session = Depends(get_db)
):
    crud_tasks.delete_task(db=db, task_id=task_id, user_id=current_user.id)


