from fastapi import FastAPI, HTTPException
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from models import UserCreate, UserLogin, User, Token, ErrorResponse
from auth import hash_password, verify_password, create_access_token
from database import users_db, current_id
import time

app = FastAPI(
    title="CrownSecure API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# Helper: get user by email
def get_user_by_email(email: str):
    for user in users_db.values():
        if user["email"] == email:
            return user
    return None

@app.post("/api/register", response_model=User)
def register(user: UserCreate):
    if get_user_by_email(user.email):
        raise HTTPException(status_code=400, detail="Email already registered")
    global current_id
    hashed_password = hash_password(user.password)
    user_data = {
        "id": current_id,
        "name": user.name,
        "email": user.email,
        "password": hashed_password,
        "job": user.job
    }
    users_db[current_id] = user_data
    current_id += 1
    return {
        "id": user_data["id"],
        "name": user_data["name"],
        "email": user_data["email"],
        "job": user_data["job"]
    }

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
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "job": user["job"]
    }

@app.put("/api/users/{user_id}", response_model=User)
def update_user(user_id: int, user_update: UserCreate):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    hashed_password = hash_password(user_update.password)
    user["name"] = user_update.name
    user["email"] = user_update.email
    user["password"] = hashed_password
    user["job"] = user_update.job
    users_db[user_id] = user
    return {
        "id": user["id"],
        "name": user["name"],
        "email": user["email"],
        "job": user["job"]
    }

@app.delete("/api/users/{user_id}")
def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted successfully"}

@app.get("/api/delay/{seconds}")
def delay(seconds: int):
    time.sleep(seconds)
    return {"message": f"Response delayed by {seconds} seconds"}
