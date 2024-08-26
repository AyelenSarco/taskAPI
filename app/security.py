
import jwt
from jwt.exceptions import InvalidTokenError
from sqlalchemy.orm import Session
from typing import Union
from datetime import datetime, timedelta, timezone
import bcrypt


# To generate a secure random secret key use the command: openssl rand -hex 32
# assigns the generated key to SECRET_KEY
SECRET_KEY = ""
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30




def verify_password(plain_password, hashed_password):
    return bcrypt.checkpw(plain_password,hashed_password)

def get_password_hash(password: str):
    return bcrypt.hashpw(password,bcrypt.gensalt(14))


def create_access_token(data:dict,expire_delta: Union[timedelta,None] = None):
    to_encode = data.copy()
    if expire_delta: 
        expire = datetime.now(timezone.utc) + expire_delta
    else:
        expire = datetime.now(timedelta.utc) + timedelta(minutes = 15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
