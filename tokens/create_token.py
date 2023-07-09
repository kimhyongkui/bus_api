from datetime import datetime, timedelta
from jose import jwt
import secrets

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = "HS256"


def create_access_token(data: dict, expires_delta: timedelta):
    payload = data.copy()
    expire = datetime.utcnow() + expires_delta
    payload.update({"exp": expire})
    encode_jwt = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


def create_refresh_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt
