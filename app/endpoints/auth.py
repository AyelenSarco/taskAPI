from fastapi import APIRouter,Depends, HTTPException,status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from ..crud import crud_users
from ..security import *
from ..deps import get_db
from ..schemas.token_schema import Token

router = APIRouter()

def authenticate_user(db:Session, username:str, password:str):
     print("authenticate user")
     user = crud_users.get_user(db=db, username=username)
     if not user:
         return False
     if not verify_password(password.encode(encoding="utf-8"), user.hashed_password):
         return False
     return user


@router.post("/token")
def login_for_access_token(
        db: Session = Depends(get_db),
        form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)
):
    print("login")
    user = authenticate_user(db=db, username=form_data.username,password=form_data.password)
    if not user:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password"
        )
    access_token_expires= timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expire_delta=access_token_expires
    )
    
    return Token(access_token=access_token, token_type="Bearer")
    
    
