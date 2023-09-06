from jose import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from tokens.create_token import SECRET_KEY, ALGORITHM
from datetime import datetime
from db.post.login import redis_client

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/bus-api/login")


def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        timestamp = datetime.utcfromtimestamp(payload["exp"])
        if timestamp < datetime.utcnow():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="만료된 토큰")

        user_id = redis_client.get(token)
        if not user_id:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="유효하지 않은 토큰")
        user_id = user_id.decode()

        return {
            "user_id": user_id,
            "token": token
        }

    except jwt.JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="자격이 검증되지 않았습니다.")

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))


def get_admin(current_user: dict = Depends(get_current_user)):
    if current_user["user_id"] != "admin":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="권한이 없습니다")
    return current_user


def verify_expired_access_token(access_token: str):
    try:
        user_id = redis_client.get(access_token)
        if not user_id:
            return None
        user_id = user_id.decode()

        refresh_token = redis_client.get(refresh_token)
        if not refresh_token:
            return None
        refresh_token = refresh_token.decode()
        return {
            "user_id": user_id,
            "access_token": access_token,
            "refresh_token": refresh_token
        }
    except Exception as err:
        return None


expired_access_token_data = verify_expired_access_token("만료된 Access Token 값")
if expired_access_token_data:
    new_access_token = create_new_access_token(expired_access_token_data["user_id"])
    redis_client.set(new_access_token, expired_access_token_data["user_id"], ex=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
    redis_client.delete(expired_access_token_data["access_token"])
    redis_client.delete(expired_access_token_data["refresh_token"])
else:
    raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
