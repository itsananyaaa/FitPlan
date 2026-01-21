# 🚀 Quick Start Guide - AI Fitness Planner

## For Windows Users (Easiest Way)

### Option 1: Double-Click Run Script

1. Open File Explorer
2. Navigate to: `c:\Users\harika kota\Downloads\fitness\fitness\fitplan__`
3. Double-click `run.bat`
4. Choose option 3 to run both Backend and Frontend
5. Streamlit will open in your browser automatically

---

## For All Users (Command Line)

### Step 1: Open Terminal/PowerShell
```
cd c:\Users\harika kota\Downloads\fitness\fitness\fitplan__
```

### Step 2: Install Dependencies
```
pip install -r requirements.txt
```

### Step 3: Start Backend (Terminal 1)
```
python run_backend.py
```

Wait for this message:
```
Starting server at http://localhost:5000
Press CTRL+C to stop the server
```

### Step 4: Start Frontend (Terminal 2)
```
streamlit run app.py
```

Wait for this message:
```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
```

---

## Testing the Integration

### Test 1: Check if Backend is Running
Open browser and go to: `http://localhost:5000/api/health`

You should see:
```json
{
  "status": "healthy",
  "service": "AI Fitness Planner Backend"
}
```

### Test 2: Use the App
1. Go to `http://localhost:8501` (should open automatically)
2. Sign up with a test account
   - Email: `test@example.com`
   - Password: `test123`
3. Fill in your fitness profile
4. See your personalized plans!

---

## Troubleshooting

### Problem: "Cannot connect to backend"
1. Check if backend is running on Terminal 1
2. Backend should be at `http://localhost:5000`
3. Restart backend: `python run_backend.py`

### Problem: Port 5000 or 8501 already in use
```bash
# Backend on different port (5001)
python -c "from backend_api import app; app.run(port=5001)"

# Frontend on different port (8502)
streamlit run app.py --server.port=8502
```

### Problem: ModuleNotFoundError
```bash
pip install -r requirements.txt --upgrade
```

### Problem: Streamlit not found
```bash
pip install streamlit>=1.40.0
```

---

## API Testing (Advanced)

### Using PowerShell

#### 1. Sign Up
```powershell
$response = Invoke-RestMethod -Uri "http://localhost:5000/api/auth/signup" `
  -Method POST `
  -ContentType "application/json" `
  -Body (@{
    name = "John Doe"
    email = "john@example.com"
    password = "password123"
  } | ConvertTo-Json)

$token = $response.access_token
Write-Output "Token: $token"
```

#### 2. Create Profile
```powershell
$response = Invoke-RestMethod -Uri "http://localhost:5000/api/profile" `
  -Method POST `
  -ContentType "application/json" `
  -Headers @{"Authorization" = "Bearer $token"} `
  -Body (@{
    age = 28
    gender = "Male"
    height_cm = 175
    weight_kg = 70
    goal = "Build muscle / strength"
    activity_level = "Moderately active"
    dietary_restrictions = "No specific restriction"
    workout_time_pref = "Morning"
  } | ConvertTo-Json)

Write-Output $response
```

#### 3. Get Exercise Plan
```powershell
$response = Invoke-RestMethod -Uri "http://localhost:5000/api/plans/exercise" `
  -Method GET `
  -Headers @{"Authorization" = "Bearer $token"}

Write-Output $response | ConvertTo-Json -Depth 10
```

---

## Using Postman (Visual Testing)

1. Download Postman: https://www.postman.com/downloads/
2. Create a new collection
3. Add requests for each API endpoint
4. Use the `Authorization` header: `Bearer {token}`

---

## File Structure

```
fitplan__/
├── app.py                 ← Streamlit Frontend
├── backend_api.py         ← Flask Backend
├── planner.py             ← Fitness Logic
├── auth.py                ← Authentication
├── requirements.txt       ← Dependencies
├── run.bat                ← Quick Start (Windows)
├── run_backend.py         ← Start Backend
├── run_frontend.py        ← Start Frontend
├── README.md              ← Full Documentation
├── QUICKSTART.md          ← This File
└── .env.example           ← Configuration Template
```

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Run backend and frontend
3. ✅ Sign up and create profile
4. ✅ View your personalized plans
5. Customize the app:
   - Edit exercises in `planner.py`
   - Add new features to backend API
   - Enhance UI in `app.py`
   - Add database integration

---

## Getting Help

- **Backend Issues**: Check `backend_api.py` terminal for error messages
- **Frontend Issues**: Check browser console (F12) for error messages
- **API Issues**: Test endpoints with Postman
- **Installation Issues**: Reinstall dependencies

---

## Key Features

✅ User Authentication (JWT)
✅ User Profiles with Health Metrics
✅ AI Personalized Exercise Plans
✅ AI Personalized Diet Plans
✅ Modern Responsive UI
✅ REST API Backend
✅ Real-time Data Validation

---

**Ready to transform your fitness journey? 🏋️💪**

Good luck! 🚀
