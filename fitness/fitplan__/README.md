# 🏋️ AI Fitness Planner - Frontend & Backend Integration Guide

## Overview

This is a complete **Streamlit Frontend + Flask Backend** integration for an AI Fitness Planning application. The frontend handles user interface and user interactions, while the backend manages authentication, user profiles, and plan generation via REST APIs.

---

## 📁 Project Structure

```
fitplan__/
├── app.py                    # Streamlit Frontend Application
├── backend_api.py            # Flask Backend API Server
├── planner.py                # Core fitness plan generation logic
├── auth.py                   # Authentication utilities (JWT)
├── requirements.txt          # Python dependencies
├── run_frontend.py           # Script to run Streamlit frontend
├── run_backend.py            # Script to run Flask backend
└── README.md                 # This file
```

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Install Dependencies

```bash
cd c:\Users\harika kota\Downloads\fitness\fitness\fitplan__
pip install -r requirements.txt
```

### Step 2: Start the Flask Backend (Terminal 1)

```bash
python run_backend.py
```

Expected output:
```
======================================================================
🏋️ AI Fitness Planner - Flask Backend API
======================================================================
Starting server at http://localhost:5000
...
Press CTRL+C to stop the server
```

### Step 3: Start the Streamlit Frontend (Terminal 2)

```bash
streamlit run app.py
```

Or use:
```bash
python run_frontend.py
```

The app will open in your browser at `http://localhost:8501`

---

## 🏗️ Architecture

### Frontend (Streamlit - `app.py`)
- User authentication (login/signup)
- User profile setup (age, gender, height, weight, goals, etc.)
- Dashboard with personalized plans
- Communicates with backend via HTTP requests
- Modern, responsive UI with custom CSS styling

### Backend (Flask - `backend_api.py`)
- REST API endpoints for all operations
- JWT token-based authentication
- In-memory database (replace with real DB in production)
- Plan generation using `planner.py` logic
- CORS-enabled for cross-origin requests

### Core Logic (`planner.py`)
- `UserProfile` dataclass for user information
- `categorize_bmi()` - BMI categorization
- `generate_exercise_plan()` - AI-powered exercise plans
- `generate_diet_plan()` - AI-powered nutrition plans

### Authentication (`auth.py`)
- JWT token creation and verification
- Token expiration handling
- Secure authentication decorator

---

## 📡 API Endpoints

### Authentication

#### 1. Login
```
POST /api/auth/login
Content-Type: application/json

{
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "access_token": "eyJ0eXAiOiJKV1QiLCJhbGc...",
  "token_type": "bearer",
  "user": {
    "email": "user@example.com"
  }
}
```

#### 2. Signup
```
POST /api/auth/signup
Content-Type: application/json

{
  "name": "John Doe",
  "email": "user@example.com",
  "password": "password123"
}

Response:
{
  "access_token": "...",
  "token_type": "bearer",
  "user": {
    "email": "user@example.com",
    "name": "John Doe"
  }
}
```

### User Profile

#### 3. Get Profile
```
GET /api/profile
Authorization: Bearer {access_token}

Response:
{
  "email": "user@example.com",
  "age": 28,
  "gender": "Male",
  "height_cm": 175,
  "weight_kg": 70,
  "bmi": 22.8,
  "goal": "Build muscle / strength",
  "activity_level": "Moderately active",
  "dietary_restrictions": "No specific restriction",
  "workout_time_pref": "Morning",
  "created_at": 1672531200,
  "updated_at": 1672531200
}
```

#### 4. Create/Update Profile
```
POST /api/profile
Authorization: Bearer {access_token}
Content-Type: application/json

{
  "age": 28,
  "gender": "Male",
  "height_cm": 175,
  "weight_kg": 70,
  "goal": "Build muscle / strength",
  "activity_level": "Moderately active",
  "dietary_restrictions": "No specific restriction",
  "workout_time_pref": "Morning"
}

Response:
{
  "message": "Profile saved successfully",
  "profile": { ... }
}
```

### Plans

#### 5. Get Exercise Plan
```
GET /api/plans/exercise
Authorization: Bearer {access_token}

Response:
{
  "email": "user@example.com",
  "goal": "Build muscle / strength",
  "activity_level": "Moderately active",
  "exercise_plan": [
    {
      "day": "Monday",
      "focus": "Full body strength",
      "details": "Compound lifts..."
    },
    ...
  ]
}
```

#### 6. Get Diet Plan
```
GET /api/plans/diet
Authorization: Bearer {access_token}

Response:
{
  "email": "user@example.com",
  "dietary_restrictions": "No specific restriction",
  "diet_plan": {
    "Breakfast": ["High-protein oatmeal...", ...],
    "Lunch": [...],
    "Snack": [...],
    "Dinner": [...],
    "Notes": ["Prioritize portion control..."]
  }
}
```

#### 7. Get Full Plan
```
GET /api/plans/full
Authorization: Bearer {access_token}

Response:
{
  "email": "user@example.com",
  "profile": { ... },
  "exercise_plan": [ ... ],
  "diet_plan": { ... }
}
```

### Utilities

#### 8. Calculate BMI
```
POST /api/calculate-bmi
Content-Type: application/json

{
  "height_cm": 175,
  "weight_kg": 70
}

Response:
{
  "height_cm": 175,
  "weight_kg": 70,
  "bmi": 22.9,
  "category": "Normal weight"
}
```

#### 9. Get BMI Category
```
GET /api/bmi-category?bmi=22.9

Response:
{
  "bmi": 22.9,
  "category": "Normal weight"
}
```

#### 10. Health Check
```
GET /api/health

Response:
{
  "status": "healthy",
  "service": "AI Fitness Planner Backend"
}
```

---

## 🔐 Authentication Flow

1. User signs up or logs in via Streamlit frontend
2. Frontend sends credentials to `/api/auth/login` or `/api/auth/signup`
3. Backend generates JWT token and returns it
4. Frontend stores token in session state
5. All subsequent requests include token in `Authorization: Bearer {token}` header
6. Backend validates token for protected endpoints
7. Token expires after 1 hour (configurable)

---

## 🎨 Frontend Features

### Authentication Page
- Login form with email and password
- Signup form with name, email, password confirmation
- Error handling for invalid credentials

### Home Page
- User profile form with fields:
  - Age, Gender, Height, Weight
  - Activity Level, Workout Time Preference
  - Fitness Goal, Dietary Restrictions
- Real-time BMI calculation
- Visual metrics display

### Dashboard Page
- Personalized weekly exercise plan
- Daily nutrition guide with meal suggestions
- Profile summary with metrics
- Edit profile option

### Styling
- Modern dark theme with gradient backgrounds
- Responsive grid layout
- Custom card components
- Color-coded elements

---

## 🔧 Configuration

### Backend Configuration (`backend_api.py`)
```python
# Change these in production!
SECRET_KEY = "CHANGE_THIS_SECRET_KEY_IN_PRODUCTION"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60  # 1 hour
```

### Frontend Configuration (`app.py`)
```python
API_URL = "http://localhost:5000/api"  # Change if backend is on different server
```

---

## 🗄️ Database

Currently uses **in-memory storage**:
- `users_db` - stores user credentials
- `profiles_db` - stores user fitness profiles

### For Production:
Replace in-memory storage with:
- PostgreSQL
- MongoDB
- Firebase
- etc.

Example PostgreSQL integration:
```python
from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://user:password@localhost/fitness_db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
```

---

## 🐛 Troubleshooting

### Issue: "Cannot connect to backend"
**Solution:** Make sure Flask server is running on port 5000
```bash
python run_backend.py
```

### Issue: Module not found errors
**Solution:** Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution:** Use different port
```bash
# Backend on different port
python -c "from backend_api import app; app.run(port=5001)"

# Frontend on different port
streamlit run app.py --server.port=8502
```

### Issue: CORS errors
**Solution:** Backend already has CORS enabled. If issues persist:
```python
# In backend_api.py
CORS(app, resources={r"/api/*": {"origins": "*"}})
```

---

## 📦 Dependencies

```
streamlit>=1.40.0      # Frontend framework
flask>=2.3.0           # Backend framework
flask-cors>=4.0.0      # CORS support
pyjwt>=2.9.0           # JWT tokens
python-dotenv>=1.0.1   # Environment variables
requests>=2.31.0       # HTTP requests
```

---

## 🚀 Deployment

### Deploy Backend (Flask)
- Use Gunicorn: `gunicorn -w 4 -b 0.0.0.0:5000 backend_api:app`
- Deploy on Heroku, AWS, DigitalOcean, etc.

### Deploy Frontend (Streamlit)
- Use Streamlit Cloud: https://streamlit.io/cloud
- Deploy on Heroku with Procfile
- Deploy on AWS, DigitalOcean, etc.

---

## 📝 Example Usage

### 1. Sign Up
```python
POST http://localhost:5000/api/auth/signup
{
  "name": "Alice Johnson",
  "email": "alice@example.com",
  "password": "SecurePass123"
}
```

### 2. Create Profile
```python
POST http://localhost:5000/api/profile
Authorization: Bearer {access_token}
{
  "age": 32,
  "gender": "Female",
  "height_cm": 165,
  "weight_kg": 65,
  "goal": "Lose fat / weight loss",
  "activity_level": "Lightly active",
  "dietary_restrictions": "Vegetarian",
  "workout_time_pref": "Evening"
}
```

### 3. Get Exercise Plan
```python
GET http://localhost:5000/api/plans/exercise
Authorization: Bearer {access_token}
```

### 4. Get Diet Plan
```python
GET http://localhost:5000/api/plans/diet
Authorization: Bearer {access_token}
```

---

## 🎯 Next Steps

1. **Add Database:** Replace in-memory storage with real database
2. **Add More Features:**
   - Progress tracking
   - Workout logging
   - Nutrition logging
   - Performance analytics
3. **Improve Security:**
   - Password hashing (bcrypt)
   - Rate limiting
   - Input validation
   - HTTPS enforcement
4. **Add More Plans:**
   - Yoga plans
   - HIIT workouts
   - Recovery routines
5. **Mobile App:** Build React Native or Flutter mobile app using same API
6. **AI Integration:** Use actual ML models for personalized recommendations

---

## 📧 Support

For issues or questions, check:
- Flask documentation: https://flask.palletsprojects.com/
- Streamlit documentation: https://docs.streamlit.io/
- JWT tutorial: https://jwt.io/

---

## 📄 License

This project is provided as-is for educational purposes.

---

**Built with ❤️ using Flask & Streamlit**
