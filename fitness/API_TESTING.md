"""
API Testing Guide - Test All Endpoints
Copy and modify these curl commands to test the backend API
"""

# ============================================================================
# SETUP - Make sure backend is running:
# python run_backend.py
# ============================================================================

# ============================================================================
# 1. HEALTH CHECK (No Auth Required)
# ============================================================================

# Test if backend is running
curl -X GET http://localhost:5000/api/health

# Expected Response:
# {
#   "status": "healthy",
#   "service": "AI Fitness Planner Backend"
# }


# ============================================================================
# 2. AUTHENTICATION - Sign Up
# ============================================================================

# Create new user account
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SecurePass123"
  }'

# Expected Response:
# {
#   "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
#   "token_type": "bearer",
#   "user": {
#     "email": "john@example.com",
#     "name": "John Doe"
#   }
# }

# Save the access_token for use in other requests
# SET TOKEN=your_access_token_here


# ============================================================================
# 3. AUTHENTICATION - Login
# ============================================================================

# Login with existing credentials
curl -X POST http://localhost:5000/api/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "john@example.com",
    "password": "SecurePass123"
  }'

# Expected Response: Same as signup


# ============================================================================
# 4. USER PROFILE - Create/Update
# ============================================================================

# Create or update user fitness profile
# Remember to replace TOKEN with actual token!

curl -X POST http://localhost:5000/api/profile \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{
    "age": 28,
    "gender": "Male",
    "height_cm": 175,
    "weight_kg": 70,
    "goal": "Build muscle / strength",
    "activity_level": "Moderately active",
    "dietary_restrictions": "Vegetarian, Gluten-free",
    "workout_time_pref": "Morning"
  }'

# Expected Response:
# {
#   "message": "Profile saved successfully",
#   "profile": {
#     "email": "john@example.com",
#     "age": 28,
#     "gender": "Male",
#     "height_cm": 175,
#     "weight_kg": 70,
#     "bmi": 22.9,
#     "goal": "Build muscle / strength",
#     "activity_level": "Moderately active",
#     "dietary_restrictions": "Vegetarian, Gluten-free",
#     "workout_time_pref": "Morning",
#     "created_at": 1672531200,
#     "updated_at": 1672531200
#   }
# }


# ============================================================================
# 5. USER PROFILE - Get
# ============================================================================

# Retrieve user fitness profile
curl -X GET http://localhost:5000/api/profile \
  -H "Authorization: Bearer TOKEN"

# Expected Response: Same profile object as above


# ============================================================================
# 6. PLANS - Get Exercise Plan
# ============================================================================

# Generate and retrieve personalized exercise plan
curl -X GET http://localhost:5000/api/plans/exercise \
  -H "Authorization: Bearer TOKEN"

# Expected Response:
# {
#   "email": "john@example.com",
#   "goal": "Build muscle / strength",
#   "activity_level": "Moderately active",
#   "exercise_plan": [
#     {
#       "day": "Monday",
#       "focus": "Full body strength",
#       "details": "Compound lifts..."
#     },
#     ...
#   ]
# }


# ============================================================================
# 7. PLANS - Get Diet Plan
# ============================================================================

# Generate and retrieve personalized diet plan
curl -X GET http://localhost:5000/api/plans/diet \
  -H "Authorization: Bearer TOKEN"

# Expected Response:
# {
#   "email": "john@example.com",
#   "dietary_restrictions": "Vegetarian, Gluten-free",
#   "diet_plan": {
#     "Breakfast": ["High-protein oatmeal...", ...],
#     "Lunch": [...],
#     "Snack": [...],
#     "Dinner": [...],
#     "Notes": ["Prioritize portion control..."]
#   }
# }


# ============================================================================
# 8. PLANS - Get Full Plan (Exercise + Diet)
# ============================================================================

# Get both exercise and diet plans at once
curl -X GET http://localhost:5000/api/plans/full \
  -H "Authorization: Bearer TOKEN"

# Expected Response: Combines exercise_plan and diet_plan in one response


# ============================================================================
# 9. UTILITIES - Calculate BMI
# ============================================================================

# Calculate BMI from height and weight
curl -X POST http://localhost:5000/api/calculate-bmi \
  -H "Content-Type: application/json" \
  -d '{
    "height_cm": 175,
    "weight_kg": 70
  }'

# Expected Response:
# {
#   "height_cm": 175,
#   "weight_kg": 70,
#   "bmi": 22.9,
#   "category": "Normal weight"
# }


# ============================================================================
# 10. UTILITIES - Get BMI Category
# ============================================================================

# Get BMI category for a given BMI value
curl -X GET "http://localhost:5000/api/bmi-category?bmi=22.9"

# Expected Response:
# {
#   "bmi": 22.9,
#   "category": "Normal weight"
# }


# ============================================================================
# COMMON ERROR RESPONSES
# ============================================================================

# 400 Bad Request - Missing required fields
# {
#   "error": "Missing required profile fields"
# }

# 401 Unauthorized - Missing or invalid token
# {
#   "error": "Token is missing"
# }
# OR
# {
#   "error": "Invalid or expired token"
# }

# 404 Not Found - Resource not found
# {
#   "error": "Profile not found. Create a profile first."
# }

# 409 Conflict - User already exists
# {
#   "error": "User already exists"
# }

# 500 Internal Server Error
# {
#   "error": "Internal server error"
# }


# ============================================================================
# TESTING IN POSTMAN
# ============================================================================

# 1. Create new collection: "AI Fitness Planner"
# 2. Add requests for each endpoint
# 3. Set environment variable: token = {{access_token}}
# 4. In signup/login request:
#    - Tests tab: pm.environment.set("access_token", pm.response.json().access_token)
# 5. Use {{token}} in Authorization header for other requests
# 6. Import this collection for quick testing


# ============================================================================
# TESTING IN POWERSHELL
# ============================================================================

# Health Check
Invoke-RestMethod -Uri "http://localhost:5000/api/health" -Method GET

# Signup
$signupResponse = Invoke-RestMethod -Uri "http://localhost:5000/api/auth/signup" `
  -Method POST -ContentType "application/json" `
  -Body (@{name="John";email="john@test.com";password="pass123"} | ConvertTo-Json)
$token = $signupResponse.access_token

# Create Profile
Invoke-RestMethod -Uri "http://localhost:5000/api/profile" `
  -Method POST -ContentType "application/json" `
  -Headers @{"Authorization"="Bearer $token"} `
  -Body (@{
    age=28;gender="Male";height_cm=175;weight_kg=70;
    goal="Build muscle / strength";activity_level="Moderately active";
    dietary_restrictions="None";workout_time_pref="Morning"
  } | ConvertTo-Json)

# Get Exercise Plan
Invoke-RestMethod -Uri "http://localhost:5000/api/plans/exercise" `
  -Method GET `
  -Headers @{"Authorization"="Bearer $token"}


# ============================================================================
# TESTING IN PYTHON
# ============================================================================

import requests

BASE_URL = "http://localhost:5000/api"

# Health check
response = requests.get(f"{BASE_URL}/health")
print(response.json())

# Signup
signup_data = {
    "name": "John Doe",
    "email": "john@example.com",
    "password": "SecurePass123"
}
response = requests.post(f"{BASE_URL}/auth/signup", json=signup_data)
token = response.json()['access_token']

# Create profile
profile_data = {
    "age": 28,
    "gender": "Male",
    "height_cm": 175,
    "weight_kg": 70,
    "goal": "Build muscle / strength",
    "activity_level": "Moderately active",
    "dietary_restrictions": "None",
    "workout_time_pref": "Morning"
}
headers = {"Authorization": f"Bearer {token}"}
response = requests.post(f"{BASE_URL}/profile", json=profile_data, headers=headers)
print(response.json())

# Get exercise plan
response = requests.get(f"{BASE_URL}/plans/exercise", headers=headers)
print(response.json())

# Get diet plan
response = requests.get(f"{BASE_URL}/plans/diet", headers=headers)
print(response.json())


# ============================================================================
# TESTING IN JAVASCRIPT/FETCH
# ============================================================================

// Health check
fetch('http://localhost:5000/api/health')
  .then(res => res.json())
  .then(data => console.log(data))

// Signup
const signupData = {
  name: 'John Doe',
  email: 'john@example.com',
  password: 'SecurePass123'
}

fetch('http://localhost:5000/api/auth/signup', {
  method: 'POST',
  headers: {'Content-Type': 'application/json'},
  body: JSON.stringify(signupData)
})
  .then(res => res.json())
  .then(data => {
    const token = data.access_token
    console.log('Token:', token)
    
    // Create profile with token
    const profileData = {
      age: 28,
      gender: 'Male',
      height_cm: 175,
      weight_cm: 70,
      goal: 'Build muscle / strength',
      activity_level: 'Moderately active',
      dietary_restrictions: 'None',
      workout_time_pref: 'Morning'
    }
    
    return fetch('http://localhost:5000/api/profile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${token}`
      },
      body: JSON.stringify(profileData)
    })
  })
  .then(res => res.json())
  .then(data => console.log('Profile created:', data))


# ============================================================================
# WORKFLOW - Complete User Journey
# ============================================================================

# 1. Start backend
python run_backend.py

# 2. Test health
curl -X GET http://localhost:5000/api/health

# 3. Signup
curl -X POST http://localhost:5000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{"name":"Test User","email":"test@example.com","password":"test123"}'
# Save TOKEN from response

# 4. Create profile
curl -X POST http://localhost:5000/api/profile \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer TOKEN" \
  -d '{
    "age": 28, "gender": "Male", "height_cm": 175, "weight_kg": 70,
    "goal": "Build muscle / strength", "activity_level": "Moderately active",
    "dietary_restrictions": "None", "workout_time_pref": "Morning"
  }'

# 5. Get plans
curl -X GET http://localhost:5000/api/plans/full \
  -H "Authorization: Bearer TOKEN"

# 6. Done! All endpoints working.


# ============================================================================
# NOTES
# ============================================================================

# - Replace TOKEN with actual JWT token from signup/login
# - All endpoints are case-sensitive
# - JSON keys are case-sensitive
# - Token expires after 1 hour
# - Login again if you get "Invalid or expired token" error
# - Profile must be created before getting plans
# - Check backend terminal for detailed error messages

