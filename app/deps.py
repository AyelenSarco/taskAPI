from .database import SessionLocal
from fastapi.security import OAuth2PasswordBearer
from typing import Annotated
import jwt
from jwt.exceptions import InvalidTokenError
from .security import SECRET_KEY, ALGORITHM
from .exceptions.exceptions import CredentialsExceptions
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session
from .models import user_model
from .schemas.user_schema import User
from .schemas.token_schema import TokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

async def get_current_user (token: Annotated[str, Depends(oauth2_scheme)], db: Session = Depends(get_db),):
     try:
         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
         username : str = payload.get("sub")
         if username is None: 
             raise CredentialsExceptions()
         token_data = TokenData(username=username)
     except InvalidTokenError:
        raise CredentialsExceptions()
     user = db.query(user_model.User).filter(user_model.User.username==token_data.username).first()
     if user is None:
         raise CredentialsExceptions()
     return user


async def get_current_active_user(
        current_user: Annotated[ User, Depends(get_current_user)]
):
    if not current_user.is_active:
        raise HTTPException(status_code=400, detail="Inactive_user")
    return current_user    