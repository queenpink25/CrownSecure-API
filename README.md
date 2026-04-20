<<<<<<< HEAD
﻿# 👑 CrownSecure API

A secure REST API with JWT authentication for user management.

## Quick Start

pip install fastapi uvicorn python-jose passlib bcrypt
python -m uvicorn main:app --reload

## API Endpoints

POST /api/register - Create account
POST /api/login - Get API key
GET /api/users/{id} - View profile
PUT /api/users/{id} - Update profile
DELETE /api/users/{id} - Delete account
GET /api/delay/{seconds} - Test latency

## Author
Asasira Queen Pinklen
=======


  #  CrownSecure API

A **secure RESTful API** with JWT authentication for user management, built with FastAPI.
    

Project Structure
CrownSecure-API/
├── main.py       # API endpoints
├── auth.py       # JWT authentication logic
├── models.py     # Pydantic data models
├── database.py   # In-memory storage
└── README.md     # Documentation

-
##  Features

- **JWT Authentication** - Secure token-based authentication
- **User Management** - Register, login, update, delete users
- **Password Hashing** - bcrypt encryption for security
- **Auto Documentation** - Interactive Swagger UI
- **Load Testing** - Built-in delay endpoint for performance testing

##  Tech Stack

- Python 3.10+
- FastAPI
- JWT (python-jose)
- bcrypt
- Uvicorn


HTTP Status Codes
Code	     Meaning	         Description
200	       ✅ Success	     Request completed successfully
400	       ❌ Bad Request	   Invalid input data
401      	 ❌ Unauthorized	 Invalid or missing API key
404	       ❌ Not Found	     Endpoint doesn't exist

## Quick Start

### Prerequisites

```bash
pip install fastapi uvicorn python-jose passlib bcrypt

Run the API
python -m uvicorn main:app --reload

Open API Documentation
http://127.0.0.1:8000/docs

API Endpoints
Method	Endpoint	             What it does
POST	  /api/register	         Create account
POST  	/api/login	           Get API key
GET	    /api/users/{id}	       View profile
PUT   	/api/users/{id}	       Update profile
DELETE	/api/users/{id}	       Delete account
GET	    /api/delay/{seconds}   Test latency

Get Your API Key
# 1. Register
curl -X POST "http://127.0.0.1:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{"name":"Your Name","email":"you@email.com","password":"123","job":"Developer"}'

# 2. Login (copy the token you receive)
curl -X POST "http://127.0.0.1:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{"email":"you@email.com","password":"123"}'

# 3. Use your token
curl -X GET "http://127.0.0.1:8000/api/users/1" \
  -H "Authorization: Bearer YOUR_TOKEN"



Authentication Guide
1️⃣ Register a User
bash
curl -X POST "http://127.0.0.1:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Your Name",
    "email": "your@email.com",
    "password": "yourpassword",
    "job": "Developer"
  }'
2️⃣ Get Your API Key (JWT Token)
bash
curl -X POST "http://127.0.0.1:8000/api/login" \
  -H "Content-Type: application/json" \
  -d '{
    "email": "your@email.com",
    "password": "yourpassword"
  }'
Response:

json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
3️⃣ Use Your API Key
bash
curl -X GET "http://127.0.0.1:8000/api/users/1" \
  -H "Authorization: Bearer YOUR_TOKEN_HERE"

📝 PowerShell Examples
Register User
powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/register" `
  -Method Post `
  -Body '{"name":"Queen","email":"queen@test.com","password":"pass123","job":"Dev"}' `
  -ContentType "application/json"

Get API Key
powershell
$response = Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/login" `
  -Method Post `
  -Body '{"email":"queen@test.com","password":"pass123"}' `
  -ContentType "application/json"
$apiKey = $response.access_token
Write-Host "Your API Key: $apiKey"


Access Protected Endpoint
powershell
$headers = @{"Authorization" = "Bearer $apiKey"}
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/users/1" `
  -Method Get `
  -Headers $headers


Update User
powershell
$headers = @{"Authorization" = "Bearer $apiKey"}
$body = '{"name":"Queen","email":"queen@test.com","password":"pass123","job":"Senior Developer"}'
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/users/1" `
  -Method Put `
  -Body $body `
  -ContentType "application/json" `
  -Headers $headers


Delete User
powershell
$headers = @{"Authorization" = "Bearer $apiKey"}
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/users/1" `
  -Method Delete `
  -Headers $headers


Test Delay Endpoint
powershell
Invoke-RestMethod -Uri "http://127.0.0.1:8000/api/delay/3" -Method Get


Quick API Test
bash
# Test if API is running
curl http://127.0.0.1:8000/api/delay/1

# Expected response:
# {"message":"Response delayed by 1 seconds"}

 Quick Test
curl http://127.0.0.1:8000/api/delay/1

Files
main.py - API endpoints

auth.py - JWT authentication

models.py - Data models

database.py - In-memory storage


Security Features
✅ Passwords hashed with bcrypt

✅ JWT tokens expire after 60 minutes

✅ Bearer token authentication required for protected routes

✅ Input validation with Pydantic


Acknowledgments
FastAPI for the amazing framework

JWT for secure authentication


Author
Asasira Queen Pinklen || Software Dev









```bash
pip install fastapi uvicorn python-jose passlib bcrypt
>>>>>>> 500b324d47a6a943a34a9019a6372869c0ee36f1
