import time
from typing import Optional

import jwt

SECRET_KEY = "CHANGE_THIS_SECRET_KEY_IN_PRODUCTION"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60  # 1 hour


def create_access_token(data: dict, expires_delta: int = ACCESS_TOKEN_EXPIRE_SECONDS) -> str:
    """
    Create a JWT access token.
    In a real app, this would be done on the backend; here we simulate it on the frontend.
    """
    to_encode = data.copy()
    expire = int(time.time()) + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def verify_token(token: str) -> Optional[dict]:
    """
    Verify a JWT and return its payload if valid, else None.
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None


def is_authenticated(session_state) -> bool:
    token = session_state.get("access_token")
    if not token:
        return False
    payload = verify_token(token)
    if payload is None:
        # Token invalid or expired
        session_state["access_token"] = None
        session_state["user"] = None
        return False
    session_state["user"] = payload.get("sub")
    return True

