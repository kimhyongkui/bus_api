from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from tokens.create_token import SECRET_KEY, ALGORITHM
from datetime import datetime

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/bus-api/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        timestamp = datetime.utcfromtimestamp(payload["exp"])
        if timestamp < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="만료된 토큰")
        return payload

    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="자격이 검증되지 않았습니다.")

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


def get_admin(current_user: dict = Depends(get_current_user)):
    if current_user["user_id"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="권한이 없습니다")
    return current_user
