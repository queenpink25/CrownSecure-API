from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from models import UserCreate, UserLogin, User, Token, ErrorResponse
from auth import hash_password, verify_password, create_access_token
from database import users_db, current_id
import time
from jose import JWTError, jwt

# Create app with explicit security scheme
app = FastAPI(
    title="CrownSecure API",
    description="Secure API with JWT Authentication",
    version="1.0.0",
    swagger_ui_parameters={"persistAuthorization": True}
)

# Define security scheme
security = HTTPBearer()

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(security)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, "crownsecure-secret-key", algorithms=["HS256"])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")
        return user_id
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid token")

def get_user_by_email(email: str):
    for user in users_db.values():
        if user["email"] == email:
            return user
    return None

# ============ ENDPOINTS ============

@app.post("/api/register", response_model=User)
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    global current_id
    hashed_password = hash_password(user.password)
    user_data = user.dict()
    user_data["password"] = hashed_password
    user_data["id"] = current_id
    users_db[current_id] = user_data
    current_id += 1
    return {k: v for k, v in user_data.items() if k != "password"}

@app.post("/api/login", response_model=Token)
def login(user: UserLogin):
    db_user = get_user_by_email(user.email)
    if not db_user:
        raise HTTPException(status_code=400, detail="User not found")
    if not verify_password(user.password, db_user["password"]):
        raise HTTPException(status_code=400, detail="Invalid password")
    token = create_access_token({"sub": str(db_user["id"])})
    return {"access_token": token, "token_type": "bearer"}

@app.get("/api/users/{user_id}", response_model=User)
def get_user(user_id: int, token_user_id: str = Depends(verify_token)):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {k: v for k, v in user.items() if k != "password"}

@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserCreate, token_user_id: str = Depends(verify_token)):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = hash_password(user_update.password)
    user.update(user_update.dict())
    user["password"] = hashed_password
    users_db[user_id] = user
    return {k: v for k, v in user.items() if k != "password"}

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int, token_user_id: str = Depends(verify_token)):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}

@app.get("/api/delay/{seconds}")
def delay(seconds: int):
    time.sleep(seconds)
    return {"message": f"Response delayed by {seconds} seconds"}