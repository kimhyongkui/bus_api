from sqlalchemy.orm import sessionmaker
from db.connection import engine
from db.models import Account
from fastapi import HTTPException, status
from app.password import verify_password
from datetime import timedelta
from tokens.create_token import create_access_token, create_refresh_token
import redis

Session = sessionmaker(bind=engine)
session = Session()

ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 30

redis_client = redis.Redis(host='localhost', port=6379)


def login(user_id, pwd):
    try:
        user = session.query(Account).filter_by(user_id=user_id, permission=True).first()
        if not user:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="아이디를 다시 확인하세요")

        if not verify_password(pwd, user.pwd):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="비밀번호가 틀렸습니다.")

        access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"user_id": user.user_id},
            expires_delta=access_token_expires
        )
        refresh_token_expires = timedelta(minutes=REFRESH_TOKEN_EXPIRE_DAYS)
        refresh_token = create_refresh_token(
            data={"user_id": user.user_id},
            expires_delta=refresh_token_expires
        )

        redis_client.set(access_token, user.user_id, ex=ACCESS_TOKEN_EXPIRE_MINUTES * 60)
        redis_client.set(refresh_token, user.user_id, ex=REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60)

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user_id": user.user_id
        }

    except HTTPException as err:
        raise err

    except Exception as err:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(err))

    finally:
        session.close()
