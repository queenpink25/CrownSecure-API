# 👑 CrownSecure API

A **secure RESTful API** with JWT authentication for user management, built with FastAPI.

## Features

- **JWT Authentication** - Secure token-based authentication
- **User Management** - Register, login, update, delete users
- **Password Hashing** - bcrypt encryption for security
- **Auto Documentation** - Interactive Swagger UI
- **Load Testing** - Built-in delay endpoint for performance testing

## Tech Stack

- Python 3.10+
- FastAPI
- JWT (python-jose)
- bcrypt
- Uvicorn

## Quick Start

### Prerequisites

```bash
pip install fastapi uvicorn python-jose passlib bcrypt

Run the API
bash
python -m uvicorn main:app --reload
Open API Documentation
text
http://127.0.0.1:8000/docs


API Endpoints
Method	     Endpoint	            Description        	Authentication
POST	       /api/register	      Create new user	    ❌ No
POST	       /api/login           Get JWT token      	❌ No
GET	         /api/users/{id}      Get user by ID     	✅ Yes
PUT          /api/users/{id}	    Update user        	✅ Yes
DELETE	     /api/users/{id}	    Delete user	        ✅ Yes
GET         /api/delay/{seconds}	Load testing	      ❌ No


Authentication Guide
1️⃣ Register a User

curl -X POST "http://127.0.0.1:8000/api/register" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Your Name",
    "email": "your@email.com",
    "password": "yourpassword",
    "job": "Developer"
  }'


2️⃣ Get Your API Key (JWT Token)

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


PowerShell Examples
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


📊 HTTP Status Codes
Code	           Meaning     	      Description
200	             ✅ Success	      Request completed successfully
400              ❌ Bad Request   	Invalid input data
401	             ❌ Unauthorized	  Invalid or missing API key
404	             ❌ Not Found	      Endpoint doesn't exist


Project Structure

CrownSecure-API/
├── main.py       # API endpoints
├── auth.py       # JWT authentication logic
├── models.py     # Pydantic data models
├── database.py   # In-memory storage
└── README.md     # Documentation

🔒 Security Features
✅ Passwords hashed with bcrypt

✅ JWT tokens expire after 60 minutes

✅ Bearer token authentication required for protected routes

✅ Input validation with Pydantic

License
MIT License - feel free to use this project for learning or production!



🙏 Acknowledgments
FastAPI for the amazing framework
JWT for secure authentication

Quick Commands Reference
Action	                 Command
Start server	           python -m uvicorn main:app --reload
Test API	               curl http://127.0.0.1:8000/api/delay/1
Register user	           curl -X POST http://127.0.0.1:8000/api/register -H "Content-Type: application/json" -d  '{"name":"Test","email":"test@test.com","password":"pass","job":"Tester"}'
Get API key	             curl -X POST http://127.0.0.1:8000/api/login -H "Content-Type: application/json" -d '{"email":"test@test.com","password":"pass"}'
Get user	               curl -X GET http://127.0.0.1:8000/api/users/1 -H "Authorization: Bearer YOUR_TOKEN"

📁 Files
main.py - API endpoints

auth.py - JWT authentication

models.py - Data models

database.py - In-memory storage


Main Functions:
1. User Registration 
People can create accounts
Passwords are encrypted (hashed with bcrypt)
Stores user info (name, email, job)

2. User Login 
Users login with email + password
System gives them a special key (JWT token)
This key proves they are who they say they are

3. API Keys (JWT Tokens) 
Each user gets a unique key after login
Key expires after 60 minutes (for security)
Key must be used to access protected features

4. User Management 👥
View user profiles
Update user information
Delete user accounts

5. Load Testing 
Special endpoint to test performance
Simulates delayed responses


Real-World Use Cases:
Example 1: Mobile App Backend
User opens app → Registers account → Gets API key 
→ App uses key to access user data → Secure!


Example 2: Web Application
Website signup → API creates account → User logs in 
→ Gets token → Accesses dashboard → All protected!

Example 3: Microservice Authentication
Service A needs user data → Requests token from CrownSecure 
→ Verifies token → Gets authorized access


 How Data Flows:
text
1. User → Sends email/password → CrownSecure
2. CrownSecure → Verifies → Returns API Key
3. User → Sends API Key with requests → CrownSecure
4. CrownSecure → Validates key → Returns user data


What It Stores:
json
{
  "id": 1,
  "name": "Queen Pinklen",
  "email": "queenpink25@gmail.com",
  "password": "hashed_encrypted_string",
  "job": "Software Engineer"
}


Who Would Use This:
User                 Why
Developers	         Authentication for their apps
Companies	           Secure employee/user management
Startups	           Quick user system for MVP
Students	           Learning API security


Why It's Valuable:
✅ Ready to use - Works immediately
✅ Secure - Industry standard practices
✅ Documented - Easy to understand
✅ Testable - Built-in test endpoints
✅ Extensible - Easy to add features


What You Can Build With It:
Social media app backend
E-commerce user system
Company employee portal
Mobile app authentication
SaaS product user management
Any app that needs user accounts!

📊 Simple Analogy:
Think of CrownSecure API as a secure building reception:

Feature	                  Analogy
Register                 	Getting a new ID card
Login	                    Scanning ID to enter
API Key	                  Your temporary access pass
Protected endpoints	      Restricted areas in building
Token expiry	            Pass expires after 60 minutes

CrownSecure API handles all the complex security stuff so you can focus on building your app!

It answers the questions:
"Is this user real?" → Registration verifies
"Who is this?" → Login identifies
"Can they access this?" → Token validates
"Is their data safe?" → Encryption protects

Author
Asasira Queen Pinklen
#   t r i g g e r   c i 
 
 
