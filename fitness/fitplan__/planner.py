from dataclasses import dataclass
from typing import List, Dict


@dataclass
class UserProfile:
    age: int
    gender: str
    height_cm: float
    weight_kg: float
    bmi: float
    goal: str
    activity_level: str
    dietary_restrictions: str
    workout_time_pref: str


def categorize_bmi(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if 18.5 <= bmi < 25:
        return "Normal weight"
    if 25 <= bmi < 30:
        return "Overweight"
    return "Obese"


def generate_exercise_plan(profile: UserProfile) -> List[Dict[str, str]]:
    intensity = {
        "Sedentary": "Low",
        "Lightly active": "Low to Moderate",
        "Moderately active": "Moderate",
        "Very active": "Moderate to High",
        "Athlete": "High",
    }.get(profile.activity_level, "Moderate")

    base_plan = [
        {
            "day": "Monday",
            "focus": "Full body strength",
            "details": "Compound lifts (squats, push-ups, rows), 3 sets of 10–12 reps.",
        },
        {
            "day": "Tuesday",
            "focus": "Cardio + Core",
            "details": "30–40 min brisk walk/jog + planks, crunches, leg raises.",
        },
        {
            "day": "Wednesday",
            "focus": "Lower body",
            "details": "Lunges, glute bridges, calf raises, 3 sets of 12–15 reps.",
        },
        {
            "day": "Thursday",
            "focus": "Active recovery",
            "details": "Light stretching, yoga, or 20–30 min easy walk.",
        },
        {
            "day": "Friday",
            "focus": "Upper body",
            "details": "Push-ups, shoulder presses, rows, bicep curls, 3 sets of 10–12 reps.",
        },
        {
            "day": "Saturday",
            "focus": "Cardio intervals",
            "details": "20–30 min interval training (1 min fast, 2 min easy).",
        },
        {
            "day": "Sunday",
            "focus": "Rest",
            "details": "Full rest or gentle stretching.",
        },
    ]

    if profile.goal == "Lose fat / weight loss":
        for d in base_plan:
            if "Cardio" in d["focus"] or "interval" in d["details"].lower():
                d["details"] += " Focus on keeping heart rate in fat-burning zone."
    elif profile.goal == "Build muscle / strength":
        for d in base_plan:
            if "strength" in d["focus"].lower() or "upper body" in d["focus"].lower():
                d["details"] += " Increase weight gradually and rest 60–90s between sets."
    elif profile.goal == "Improve overall fitness":
        for d in base_plan:
            d["details"] += " Keep intensity at a comfortable but challenging level."

    if profile.workout_time_pref in ["Morning", "Evening"]:
        for d in base_plan:
            d["details"] += f" Best done in the {profile.workout_time_pref.lower()} based on your preference."

    return base_plan


def generate_diet_plan(profile: UserProfile) -> Dict[str, List[str]]:
    bmi_category = categorize_bmi(profile.bmi)

    base_meals = {
        "Breakfast": [
            "High-protein oatmeal with nuts and seeds",
            "Greek yogurt with berries",
            "Vegetable omelette with whole-grain toast",
        ],
        "Lunch": [
            "Grilled chicken / tofu bowl with brown rice and veggies",
            "Mixed bean salad with olive oil dressing",
            "Whole-grain wrap with lean protein and salad",
        ],
        "Snack": [
            "Handful of nuts or seeds",
            "Fruit with peanut butter or hummus",
            "Protein smoothie with spinach and banana",
        ],
        "Dinner": [
            "Baked fish / paneer with quinoa and steamed veggies",
            "Stir-fry with colorful vegetables and lean protein",
            "Lentil curry with brown rice and salad",
        ],
    }

    if "veg" in profile.dietary_restrictions.lower():
        for key, meals in base_meals.items():
            base_meals[key] = [m.replace("chicken", "tofu").replace("fish", "paneer") for m in meals]

    if "vegan" in profile.dietary_restrictions.lower():
        replacements = {
            "yogurt": "soy yogurt",
            "Greek yogurt": "soy yogurt",
            "paneer": "tofu",
            "milk": "plant milk",
        }
        for key, meals in base_meals.items():
            new_meals = []
            for m in meals:
                for src, dst in replacements.items():
                    if src.lower() in m.lower():
                        m = m.replace(src, dst)
                new_meals.append(m)
            base_meals[key] = new_meals

    if profile.goal == "Lose fat / weight loss":
        note = " Prioritize portion control and high-fiber foods to keep you full."
    elif profile.goal == "Build muscle / strength":
        note = " Emphasize high-protein options and include a source of protein at every meal."
    else:
        note = " Aim for balanced meals with lean protein, complex carbs, and healthy fats."

    if bmi_category in ["Overweight", "Obese"]:
        note += " Reduce sugary drinks and highly processed foods."
    elif bmi_category == "Underweight":
        note += " Add calorie-dense healthy foods like nuts, seeds, and healthy oils."

    base_meals["Notes"] = [note]
    return base_meals

