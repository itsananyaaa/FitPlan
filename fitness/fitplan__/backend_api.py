from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app)

app.config["SECRET_KEY"] = "zenflow-secret-key"

# ===============================
# IN-MEMORY DATABASE
# ===============================
users_db = {}

# ===============================
# DIET DATABASE
# ===============================
DIET_PLANS = {
    "Vegetarian": {
        "Breakfast": "Oatmeal with nuts and honey",
        "Lunch": "Chickpea salad with lemon-tahini dressing",
        "Snack": "Greek yogurt with berries",
        "Dinner": "Lentil curry with brown rice"
    },
    "Vegan": {
        "Breakfast": "Tofu scramble with spinach",
        "Lunch": "Quinoa and black bean bowl",
        "Snack": "Apple slices with peanut butter",
        "Dinner": "Roasted cauliflower tacos"
    },
    "Keto": {
        "Breakfast": "3-egg omelet with avocado",
        "Lunch": "Grilled salmon with buttered asparagus",
        "Snack": "Handful of macadamia nuts",
        "Dinner": "Chicken thighs with cheesy broccoli"
    },
    "Paleo": {
        "Breakfast": "Sweet potato hash with eggs",
        "Lunch": "Grilled chicken breast with mixed greens",
        "Snack": "Beef jerky and almonds",
        "Dinner": "Steak with roasted carrots and zucchini"
    },
    "Balanced": {
        "Breakfast": "Whole grain toast with eggs",
        "Lunch": "Turkey and avocado wrap",
        "Snack": "Cottage cheese and pineapple",
        "Dinner": "Baked cod with quinoa and green beans"
    }
}

# ===============================
# WORKOUT DATABASE (NEW)
# ===============================
WORKOUT_PLANS = {
    "Strength": { # Mapped to Keto/Paleo/Balanced
        "Monday": "Chest & Tricots (Bench Press, Pushups, Dips)",
        "Tuesday": "Back & Biceps (Pull-ups, Rows, Curls)",
        "Wednesday": "Leg Day (Squats, Lunges, Calf Raises)",
        "Thursday": "Active Recovery (20 min Walk + Stretching)",
        "Friday": "Shoulders & Core (Overhead Press, Planks, Leg Raises)",
        "Saturday": "HIIT (Sprints or Jump Rope - 20 mins)",
        "Sunday": "Full Rest Day"
    },
    "Endurance/Flexibility": { # Mapped to Vegan/Vegetarian
        "Monday": "Long Distance Run or Fast Walk (30-45 mins)",
        "Tuesday": "Full Body Yoga & Mobility Flow",
        "Wednesday": "Bodyweight Circuit (Burpees, Squats, Mountain Climbers)",
        "Thursday": "Cycling or Swimming (30 mins)",
        "Friday": "Pilates or Core-specific routine",
        "Saturday": "Outdoor Activity (Hiking or Long Walk)",
        "Sunday": "Deep Stretching & Meditation"
    }
}

# ===============================
# PLAN GENERATION ENDPOINT
# ===============================
@app.route("/api/generate-plan", methods=["POST"])
def generate_plan():
    data = request.get_json(force=True)
    
    try:
        age = int(data.get("age"))
        weight = float(data.get("weight"))
        height = float(data.get("height"))
        gender = data.get("gender")
        preference = data.get("dietary_preference", "Balanced")
    except (TypeError, ValueError):
        return jsonify({"message": "Invalid physical data provided"}), 400

    # 1. Calculate BMR (Mifflin-St Jeor)
    if gender.lower() == "male":
        bmr = (10 * weight) + (6.25 * height) - (5 * age) + 5
    else:
        bmr = (10 * weight) + (6.25 * height) - (5 * age) - 161

    # 2. Calculate TDEE
    tdee = int(bmr * 1.375)

    # 3. Macro Split
    protein = int((tdee * 0.30) / 4)
    carbs = int((tdee * 0.45) / 4)
    fats = int((tdee * 0.25) / 9)

    # 4. Logic for Workout Mapping
    # If the user chooses a high-fat/meat diet, give them Strength. 
    # Otherwise, give them Endurance/Flexibility.
    if preference in ["Keto", "Paleo", "Balanced"]:
        selected_workout = WORKOUT_PLANS["Strength"]
    else:
        selected_workout = WORKOUT_PLANS["Endurance/Flexibility"]

    return jsonify({
        "nutritional_plan": {
            "daily_calories": tdee,
            "macros": {
                "protein_g": protein,
                "carbs_g": carbs,
                "fats_g": fats
            }
        },
        "diet_plan": DIET_PLANS.get(preference, DIET_PLANS["Balanced"]),
        "workout_plan": selected_workout, # NEW KEY
        "preference_applied": preference
    }), 200

# (Keep your existing signup/login routes here...)

@app.route("/api/auth/signup", methods=["POST"])
def signup():
    data = request.get_json(force=True)
    email = data.get("email", "").strip().lower()
    if email in users_db:
        return jsonify({"message": "User already exists"}), 409
    users_db[email] = data
    return jsonify({"message": "Signup successful"}), 201

@app.route("/api/auth/login", methods=["POST"])
def login():
    data = request.get_json(force=True)
    identifier = (data.get("email") or data.get("username", "")).strip().lower()
    password = data.get("password")
    
    user = users_db.get(identifier)
    if not user:
        for u in users_db.values():
            if u["username"].lower() == identifier:
                user = u
                break

    if not user or user["password"] != password:
        return jsonify({"message": "Invalid credentials"}), 401

    token = jwt.encode(
        {"email": user["email"], "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)},
        app.config["SECRET_KEY"], algorithm="HS256"
    )
    return jsonify({"access_token": token, "username": user["username"]}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)