from tokens.create_token import create_access_token
from datetime import timedelta
from dotenv import load_dotenv
import redis
import os

load_dotenv()

redis_client = redis.Redis(host=os.getenv("HOST"), port=6379)


def refresh_access_token(data: dict, expires_delta: timedelta, user_id):
    refresh_token_key = "refresh_token:" + user_id
    refresh_token = redis_client.get(refresh_token_key)
    if refresh_token is None:
        return None

    new_access_token = create_access_token(data, expires_delta)

    access_token_key = "access_token:" + user_id
    redis_client.set(access_token_key, new_access_token, ex=expires_delta.total_seconds())

    return new_access_token
