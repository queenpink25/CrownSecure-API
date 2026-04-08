# 👑 CrownSecure API

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
