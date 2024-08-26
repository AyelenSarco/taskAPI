from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas.user_schema import User,UserCreate
from ..crud import crud_users, crud_tasks
from typing import Annotated
from ..deps import get_db,get_current_active_user


router = APIRouter()


@router.post("/user/create/", response_model=User)
async def create_user(user: UserCreate,db: Session = Depends(get_db)):
    
    
    return crud_users.create_user(db=db, user=user)
    

@router.get("/user/me/", response_model= User)
async def read_user_me(
    current_user: Annotated [User, Depends(get_current_active_user)]
):
    return current_user

@router.delete("/user/delete")
async def delete_user(
    current_user: Annotated[User,Depends(get_current_active_user)],
    db : Session = Depends(get_db)
):
    crud_tasks.delete_tasks_from_user(db=db, user_id=current_user.id)
    crud_users.delete_user(db, current_user.id)