from jose import jwt, JWTError
from fastapi import Depends, HTTPException, Header

CLERK_PUBLIC_KEY = "your-clerk-public-key"

def verify_token(authorization: str = Header(...)):
    try:
        token = authorization.split(" ")[1]
        payload = jwt.decode(token, CLERK_PUBLIC_KEY, algorithms=["RS256"])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or missing token")

def get_current_user(token_payload: dict = Depends(verify_token)):
    return {"user_id": token_payload["sub"], "email": token_payload["email"]}