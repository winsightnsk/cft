from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from typing import Optional
from datetime import datetime, timedelta
from jose import jwt
from jose.exceptions import JWTError
from sqlalchemy.orm.session import Session
from db.database import get_db
from db import db_user
from fastapi import HTTPException, status


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

SECRET_KEY = '6fd1ff33024ae687337177ff096359b44bd3b40917fd4df6667a74879775b18b'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
  to_encode = data.copy()
  if expires_delta:
    expire = datetime.utcnow() + expires_delta
  else:
    expire = datetime.utcnow() + timedelta(minutes=15)
  to_encode.update({"exp": expire})
  encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
  return encoded_jwt

def get_user_by_token(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db) ):
  credetials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail='Невалидно',
    headers={"WWW-Authenticate": "Bearer"},
  )
  try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    fromtoken: str = payload.get('sub')
    if fromtoken is None:
      raise credetials_exception
  except JWTError:
    raise credetials_exception

  user = db_user.get_user(db, int(fromtoken))

  if user is None:
    raise credetials_exception

  return user