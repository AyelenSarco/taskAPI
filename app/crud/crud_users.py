from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from ..schemas import user_schema
from ..models import user_model
from ..security import get_password_hash
from ..exceptions.exceptions import NotFoundException, InvalidInputException, DataBaseException

def create_user (db:Session, user: user_schema.UserCreate):
    existing_user = db.query(user_model.User).filter(user_model.User.username==user.username).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username already registered")
    if not user.username:
        raise InvalidInputException("Username is required")
    if not user.password:
        raise InvalidInputException("Password is required")
    print('Hashing password')
    hashed_password = get_password_hash(user.password.encode(encoding="utf-8"))
    print('Password hashed')
    try:
        print('Adding user')
        db_user = user_model.User(username = user.username, hashed_password = hashed_password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        print('User added')
    except Exception as e:
        print('databaseException')
        raise DataBaseException(str(e))
    
    print(db_user.id, db_user.username, db_user.is_active)   
    return db_user



def get_user(db:Session, username: str):
    return db.query(user_model.User).filter(user_model.User.username==username).first()


def delete_user(db:Session, user_id: int):
    db_user = db.query(user_model.User).filter(user_model.User.id==user_id).first()
    try:
        db.delete(db_user)
        db.commit()
    except Exception as e:
        raise DataBaseException(str(e))
    
