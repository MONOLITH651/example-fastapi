from fastapi.param_functions import Depends
from jose import JWTError, jwt
from datetime import datetime, timedelta

from sqlalchemy.orm import Session
from . import schemas,database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .config import settings


oath2_scheme = OAuth2PasswordBearer(tokenUrl="login")


SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes

def create_access_token(data: dict):
    to_encode = data.copy()
    # we don't wont to overwrite data so we copying it
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt  = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # decoding jwt
        id: str = payload.get("user_id")
        #extracting id from payload
        if id is None:
            raise credentials_exception
            # if no id we will throw an error
        token_data = schemas.TokenData(id=id)
        # validating with schema actual token data that in this case is just id, you can add more if needed
        # also we returning token data to make sure we can use it
    except JWTError:
        raise credentials_exception

    return token_data
    # nothing more than id that then returns back but get_current_user function

def get_current_user(token: str = Depends(oath2_scheme), db: Session = Depends(database.get_db)):
    # function that actually calls verify_access token
    # also designed to fetch the user id or token_data
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
    detail= F"could not validate credentials", headers= {"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()
    # query your db to grab the user
    print(user)

    return user
    # returning the user
     # it will take the token from the request automatically
# extract id for us
# it's going to verify that the token is correct by calling verify_access_ token function
# will extract id