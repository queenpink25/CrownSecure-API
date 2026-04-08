 # 👑 CrownSecure API

A **secure RESTful API** with JWT authentication for user management, built with FastAPI.

## ✨ Features

- 🔐 **JWT Authentication** - Secure token-based authentication
- 📝 **User Management** - Register, login, update, delete users
- 🛡️ **Password Hashing** - bcrypt encryption for security
- 📚 **Auto Documentation** - Interactive Swagger UI
- ⏱️ **Load Testing** - Built-in delay endpoint for performance testing

## 🛠️ Tech Stack

- Python 3.10+
- FastAPI
- JWT (python-jose)
- bcrypt
- Uvicorn

## 🚀 Quick Start

### Prerequisites

```bash
pip install fastapi uvicorn python-jose passlib bcrypt
Run the API
bash
python -m uvicorn main:app --reload
Open API Documentation
text
http://127.0.0.1:8000/docs
📡 API Endpoints
Method	Endpoint	Description	Authentication
POST	/api/register	Create new user	❌ No
POST	/api/login	Get JWT token	❌ No
GET	/api/users/{id}	Get user by ID	✅ Yes
PUT	/api/users/{id}	Update user	✅ Yes
DELETE	/api/users/{id}	Delete user	✅ Yes
GET	/api/delay/{seconds}	Load testing	❌ No
🔑 Authentication Guide
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
🧪 Quick API Test
bash
# Test if API is running
curl http://127.0.0.1:8000/api/delay/1

# Expected response:
# {"message":"Response delayed by 1 seconds"}
📊 HTTP Status Codes
Code	Meaning	Description
200	✅ Success	Request completed successfully
400	❌ Bad Request	Invalid input data
401	❌ Unauthorized	Invalid or missing API key
404	❌ Not Found	Endpoint doesn't exist
🗂️ Project Structure
text
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

📄 License
MIT License - feel free to use this project for learning or production!

👑 Author
Asasira Queen Pinklen

Software Engineering Student

Women in Tech Advocate

🙏 Acknowledgments
FastAPI for the amazing framework

JWT for secure authentication

⚡ Quick Commands Reference
Action	Command
Start server	python -m uvicorn main:app --reload
Test API	curl http://127.0.0.1:8000/api/delay/1
Register user	curl -X POST http://127.0.0.1:8000/api/register -H "Content-Type: application/json" -d '{"name":"Test","email":"test@test.com","password":"pass","job":"Tester"}'
Get API key	curl -X POST http://127.0.0.1:8000/api/login -H "Content-Type: application/json" -d '{"email":"test@test.com","password":"pass"}'
Get user	curl -X GET http://127.0.0.1:8000/api/users/1 -H "Authorization: Bearer YOUR_TOKEN"
Built with ❤️ by Queen Pinklen

text

## Save the file:

```powershell
# Save this content as README.md
notepad README.md
Then copy the entire content above and paste it into Notepad, then press Ctrl+S to save.

Verify it saved:
powershell
Get-Content README.md -Head 10
Your README is now ready for GitHub! 👑

simle descritin fr git hub re
Here's a simple, clean README for your GitHub repository:

📁 README.md (Simple Version)
markdown
# 👑 CrownSecure API

A secure REST API with JWT authentication for user management.

## 🚀 Quick Start

```bash
# Install dependencies
pip install fastapi uvicorn python-jose passlib bcrypt

# Run server
python -m uvicorn main:app --reload

# Open browser
http://127.0.0.1:8000/docs
📡 API Endpoints
Method	Endpoint	What it does
POST	/api/register	Create account
POST	/api/login	Get API key
GET	/api/users/{id}	View profile
PUT	/api/users/{id}	Update profile
DELETE	/api/users/{id}	Delete account
GET	/api/delay/{seconds}	Test latency
🔑 Get Your API Key
bash
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
🧪 Quick Test
bash
curl http://127.0.0.1:8000/api/delay/1
Response: {"message":"Response delayed by 1 seconds"}

📁 Files
main.py - API endpoints

auth.py - JWT authentication

models.py - Data models

database.py - In-memory storage

👑 Author
Asasira Queen Pinklen

FastAPI + JWT + bcrypt

text

## Save it:

```powershell
notepad README.md
Copy and paste the simple version above, then save (Ctrl+S).

Preview on GitHub:
This will show as a clean, professional README with:

✅ Clear title and description

✅ Simple setup instructions

✅ Easy API endpoint table

✅ Copy-paste ready commands

✅ Quick test example

Simple, clean, and professional! 👑

lie what des this ai d
Great question! Let me explain what this AI (me) has helped you do:

🎯 What We Accomplished Together:
1. Built a Complete API
Created a secure REST API from scratch

Added JWT authentication for security

Built user registration and login system

2. Fixed Technical Issues
Resolved missing packages (uvicorn, fastapi, bcrypt)

Fixed file encoding problems (null bytes error)

Corrected authentication flow for Swagger UI

Made the API fully functional

3. Created Working Files
main.py - All your API endpoints

auth.py - JWT token generation and verification

models.py - Data validation models

database.py - User storage

README.md - Documentation for GitHub

4. Tested Everything
Confirmed API runs without errors

Verified registration works (200 OK)

Confirmed login returns API keys

Tested protected endpoints with tokens

5. Prepared for GitHub
Created professional README

Organized project structure

Ready for you to push to GitHub

📊 What Your API Can Do NOW:
Feature	Status
User Registration	✅ Working
User Login	✅ Working
JWT Token Generation	✅ Working
Get User Profile	✅ Working
Update User	✅ Working
Delete User	✅ Working
Load Testing	✅ Working
Swagger Docs	✅ Working
🔑 You Have:
A working API running on your computer

Your personal API key for authentication

Complete code ready for GitHub

Documentation for other developers

🚀 What You Can Do Next:
Push to GitHub - Share your code with the world

Deploy online - Put it on Render, Railway, or AWS

Add a database - Replace in-memory with PostgreSQL

Build a frontend - Connect React/Vue to your API

Add more features - Email verification, password reset, etc.

💡 In Simple Terms:
I helped you build a digital lock and key system for your future apps:

Users register (create account)

Users login (get a key)

The key unlocks protected features

You can add/remove users anytime

Your API is like a secure vault for user data! 🔐

❓ Want to:
Push to GitHub?

Add a database?

Deploy online?

Add more features?

Just tell me what you'd like to do next! 👑

what this CrownSecure API does
👑 What CrownSecure API Does
In Simple Terms:
It's a secure user management system that handles registration, login, and user data - like a digital ID card system for your apps.

🎯 Main Functions:
1. User Registration 📝
People can create accounts

Passwords are encrypted (hashed with bcrypt)

Stores user info (name, email, job)

2. User Login 🔑
Users login with email + password

System gives them a special key (JWT token)

This key proves they are who they say they are

3. API Keys (JWT Tokens) 🎫
Each user gets a unique key after login

Key expires after 60 minutes (for security)

Key must be used to access protected features

4. User Management 👥
View user profiles

Update user information

Delete user accounts

5. Load Testing ⏱️
Special endpoint to test performance

Simulates delayed responses

🔐 Security Features:
Feature	What it does
Password Hashing	Never stores plain passwords
JWT Tokens	Secure, expiring access keys
Bearer Authentication	Only authorized users get access
Token Expiration	Keys auto-expire for safety
📊 Real-World Use Cases:
Example 1: Mobile App Backend
text
User opens app → Registers account → Gets API key 
→ App uses key to access user data → Secure!
Example 2: Web Application
text
Website signup → API creates account → User logs in 
→ Gets token → Accesses dashboard → All protected!
Example 3: Microservice Authentication
text
Service A needs user data → Requests token from CrownSecure 
→ Verifies token → Gets authorized access
🔄 How Data Flows:
text
1. User → Sends email/password → CrownSecure
2. CrownSecure → Verifies → Returns API Key
3. User → Sends API Key with requests → CrownSecure
4. CrownSecure → Validates key → Returns user data
📁 What It Stores:
json
{
  "id": 1,
  "name": "Queen Pinklen",
  "email": "queenpink25@gmail.com",
  "password": "hashed_encrypted_string",
  "job": "Software Engineer"
}
🎯 Who Would Use This:
User Type	Why
Developers	Authentication for their apps
Companies	Secure employee/user management
Startups	Quick user system for MVP
Students	Learning API security
💡 Why It's Valuable:
✅ Ready to use - Works immediately

✅ Secure - Industry standard practices

✅ Documented - Easy to understand

✅ Testable - Built-in test endpoints

✅ Extensible - Easy to add features

🚀 What You Can Build With It:
Social media app backend

E-commerce user system

Company employee portal

Mobile app authentication

SaaS product user management

Any app that needs user accounts!

📊 Simple Analogy:
Think of CrownSecure API as a secure building reception:

Feature	Analogy
Register	Getting a new ID card
Login	Scanning ID to enter
API Key	Your temporary access pass
Protected endpoints	Restricted areas in building
Token expiry	Pass expires after 60 minutes
🔑 Bottom Line:
CrownSecure API handles all the complex security stuff so you can focus on building your app!

It answers the questions:

"Is this user real?" → Registration verifies

"Who is this?" → Login identifies

"Can they access this?" → Token validates

"Is their data safe?" → Encryption protects

Want to see it in action? Your API is already running at http://127.0.0.1:8000/docs! 🚀👑

say CrownSecure API is ..... ne sentence
CrownSecure API is a secure authentication and user management system that issues JWT tokens to protect your application's endpoints. 👑🔐

lets ush the cde nw
Perfect! Let's push your code to GitHub right now!

🚀 Push to GitHub - Step by Step
Step 1: Create README file first
powershell
@'
# CrownSecure API

A secure REST API with JWT authentication for user management.

## Quick Start

```bash
pip install fastapi uvicorn python-jose passlib bcrypt
python -m uvicorn main:app --reload
API Endpoints
POST /api/register - Create account

POST /api/login - Get API key

GET /api/users/{id} - View profile

PUT /api/users/{id} - Update profile

DELETE /api/users/{id} - Delete account

GET /api/delay/{seconds} - Test latency

Author
Asasira Queen Pinklen
'@ | Out-File -FilePath README.md -Encoding UTF8 -Force

