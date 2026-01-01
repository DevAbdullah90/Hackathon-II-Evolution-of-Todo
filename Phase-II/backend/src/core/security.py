from fastapi import Depends, HTTPException, status, Request
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import jwt
import os
from dotenv import load_dotenv
from sqlmodel import Session as DBSession, select
from ..core.database import get_session
from ..models.auth_session import Session as AuthSession
from datetime import datetime

load_dotenv()

BETTER_AUTH_SECRET = os.getenv("BETTER_AUTH_SECRET")
ALGORITHM = "HS256"

security = HTTPBearer(auto_error=False)

def verify_token(
    request: Request = None, 
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: DBSession = Depends(get_session)
) -> str:
    """
    Verifies the token (JWT or Opaque) and returns the user_id.
    """
    token = None
    if credentials:
        print(f"DEBUG: Found credentials in header")
        token = credentials.credentials
        print(f"DEBUG: Token content: '{token}'")
    elif request:
         token = request.cookies.get("better-auth.session_token") or request.cookies.get("taskoo-v2.session_token")
    
    if not token:
          print("DEBUG: No token found")
          raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate credentials: no token found",
                headers={"WWW-Authenticate": "Bearer"},
            )
    
    # 1. Try JWT
    if BETTER_AUTH_SECRET:
        try:
            # Only attempt if it looks like a JWT to avoid log spam
            if token.startswith("ey"):
                print(f"DEBUG: Attempting to decode JWT...")
                payload = jwt.decode(token, BETTER_AUTH_SECRET, algorithms=[ALGORITHM])
                user_id = payload.get("sub") or payload.get("id") or payload.get("user_id")
                if user_id:
                    return user_id
        except jwt.PyJWTError as e:
            print(f"DEBUG: JWT Decode Error: {str(e)}. Falling back to DB check.")

    # 2. Fallback to Opaque/DB Token
    print(f"DEBUG: Checking DB for opaque token: {token}")
    statement = select(AuthSession).where(AuthSession.token == token)
    session_record = db.exec(statement).first()

    if session_record:
        if session_record.expiresAt > datetime.now():
            print(f"DEBUG: Valid opaque session found for user {session_record.userId}")
            return session_record.userId
        else:
            print("DEBUG: Session expired")
    else:
        print("DEBUG: No session record found in DB")

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

get_current_user = verify_token
