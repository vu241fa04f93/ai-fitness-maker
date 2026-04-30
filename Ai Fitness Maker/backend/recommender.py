from __future__ import annotations

from copy import deepcopy

from .schemas import Exercise, Meal, Precaution, RecommendationResponse, UserProfileCreate


BASE_PLANS = {
    "lose": {
        "calorie_factor": 26,
        "meals": [
            {
                "time": "Breakfast",
                "name": "Lean Start",
                "items": ["Oats", "Low-fat milk", "Boiled eggs", "Apple"],
                "calories": 320,
                "protein_g": 24,
                "carbs_g": 36,
                "fat_g": 8,
            },
            {
                "time": "Lunch",
                "name": "Protein Plate",
                "items": ["Grilled chicken", "Brown rice", "Mixed salad"],
                "calories": 440,
                "protein_g": 38,
                "carbs_g": 42,
                "fat_g": 10,
            },
            {
                "time": "Evening",
                "name": "Light Snack",
                "items": ["Greek yogurt", "Banana", "Chia seeds"],
                "calories": 230,
                "protein_g": 17,
                "carbs_g": 25,
                "fat_g": 6,
            },
            {
                "time": "Dinner",
                "name": "Clean Finish",
                "items": ["Paneer or fish", "Sauteed vegetables", "Soup"],
                "calories": 390,
                "protein_g": 34,
                "carbs_g": 22,
                "fat_g": 13,
            },
        ],
        "exercises": [
            {
                "name": "Squats",
                "sets": "4 x 15 reps",
                "muscle": "Legs, Glutes",
                "type": "Strength",
                "difficulty": "Medium",
                "detector_id": "squat",
            },
            {
                "name": "Push-ups",
                "sets": "3 x 12 reps",
                "muscle": "Chest, Core",
                "type": "Strength",
                "difficulty": "Medium",
                "detector_id": "pushup",
            },
            {
                "name": "Lunges",
                "sets": "3 x 12 reps each leg",
                "muscle": "Legs",
                "type": "Strength",
                "difficulty": "Medium",
                "detector_id": "lunge",
            },
        ],
        "precautions": [
            {
                "title": "Avoid crash dieting",
                "text": "Maintain a moderate calorie deficit so energy and muscle mass are preserved.",
            },
            {
                "title": "Track recovery",
                "text": "Fat loss stalls when sleep and hydration are poor. Target 7-8 hours of sleep.",
            },
        ],
    },
    "gain": {
        "calorie_factor": 34,
        "meals": [
            {
                "time": "Breakfast",
                "name": "Mass Builder",
                "items": ["Milk", "Peanut butter toast", "Eggs", "Banana"],
                "calories": 520,
                "protein_g": 30,
                "carbs_g": 50,
                "fat_g": 20,
            },
            {
                "time": "Lunch",
                "name": "Heavy Lunch",
                "items": ["Chicken or paneer", "Rice", "Curd", "Vegetables"],
                "calories": 640,
                "protein_g": 42,
                "carbs_g": 70,
                "fat_g": 18,
            },
            {
                "time": "Evening",
                "name": "Recovery Snack",
                "items": ["Protein shake", "Dates", "Nuts"],
                "calories": 360,
                "protein_g": 28,
                "carbs_g": 24,
                "fat_g": 14,
            },
            {
                "time": "Dinner",
                "name": "Growth Dinner",
                "items": ["Fish or dal", "Chapati", "Potato", "Salad"],
                "calories": 560,
                "protein_g": 34,
                "carbs_g": 60,
                "fat_g": 16,
            },
        ],
        "exercises": [
            {
                "name": "Squats",
                "sets": "4 x 10 reps",
                "muscle": "Legs, Core",
                "type": "Compound",
                "difficulty": "Hard",
                "detector_id": "squat",
            },
            {
                "name": "Push-ups",
                "sets": "4 x 15 reps",
                "muscle": "Chest, Triceps",
                "type": "Compound",
                "difficulty": "Medium",
                "detector_id": "pushup",
            },
            {
                "name": "Bicep Curls",
                "sets": "3 x 12 reps",
                "muscle": "Biceps",
                "type": "Isolation",
                "difficulty": "Easy",
                "detector_id": "curl",
            },
        ],
        "precautions": [
            {
                "title": "Use progressive overload",
                "text": "Increase reps or resistance gradually to create measurable muscle stimulus.",
            },
            {
                "title": "Prioritize protein",
                "text": "Target 1.6-2.2 g protein per kg body weight across the day.",
            },
        ],
    },
    "maintain": {
        "calorie_factor": 30,
        "meals": [
            {
                "time": "Breakfast",
                "name": "Balanced Start",
                "items": ["Eggs", "Toast", "Yogurt", "Fruit"],
                "calories": 380,
                "protein_g": 24,
                "carbs_g": 35,
                "fat_g": 12,
            },
            {
                "time": "Lunch",
                "name": "Balanced Plate",
                "items": ["Chicken or tofu", "Quinoa", "Salad"],
                "calories": 500,
                "protein_g": 36,
                "carbs_g": 42,
                "fat_g": 14,
            },
            {
                "time": "Evening",
                "name": "Smart Snack",
                "items": ["Fruit", "Almonds", "Green tea"],
                "calories": 220,
                "protein_g": 8,
                "carbs_g": 18,
                "fat_g": 12,
            },
            {
                "time": "Dinner",
                "name": "Light Dinner",
                "items": ["Fish or dal", "Vegetables", "Rice"],
                "calories": 420,
                "protein_g": 28,
                "carbs_g": 35,
                "fat_g": 11,
            },
        ],
        "exercises": [
            {
                "name": "Plank",
                "sets": "3 x 60 sec",
                "muscle": "Core",
                "type": "Stability",
                "difficulty": "Medium",
                "detector_id": "plank",
            },
            {
                "name": "Squats",
                "sets": "3 x 15 reps",
                "muscle": "Legs",
                "type": "Strength",
                "difficulty": "Medium",
                "detector_id": "squat",
            },
            {
                "name": "Push-ups",
                "sets": "3 x 12 reps",
                "muscle": "Chest, Core",
                "type": "Strength",
                "difficulty": "Medium",
                "detector_id": "pushup",
            },
        ],
        "precautions": [
            {
                "title": "Keep routine consistent",
                "text": "Maintenance depends more on consistency than aggressive diet or training changes.",
            },
            {
                "title": "Monitor stress and sleep",
                "text": "Poor recovery can still reduce performance even when the goal is maintenance.",
            },
        ],
    },
}


def calculate_bmi(weight_kg: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return round(weight_kg / (height_m * height_m), 1)


def bmi_status(bmi: float) -> str:
    if bmi < 18.5:
        return "Underweight"
    if bmi < 25:
        return "Normal"
    if bmi < 30:
        return "Overweight"
    return "Obese"


def recommend_plan(profile: UserProfileCreate) -> RecommendationResponse:
    plan = deepcopy(BASE_PLANS[profile.goal])
    bmi = calculate_bmi(profile.weight_kg, profile.height_cm)
    status = bmi_status(bmi)
    daily_calories = round(profile.weight_kg * plan["calorie_factor"])

    notes = [
        f"BMI classification: {status}",
        f"Daily calorie target estimated from body weight and goal: {daily_calories} kcal/day",
    ]

    if status == "Underweight" and profile.goal == "lose":
        notes.append("Goal conflict detected: weight loss is not recommended for underweight users.")
    if status in {"Overweight", "Obese"} and profile.goal == "gain":
        notes.append("Goal conflict detected: body gain should be supervised if the user is already overweight.")

    return RecommendationResponse(
        bmi=bmi,
        bmi_status=status,
        goal=profile.goal,
        daily_calories=daily_calories,
        meals=[Meal(**meal) for meal in plan["meals"]],
        exercises=[Exercise(**exercise) for exercise in plan["exercises"]],
        precautions=[Precaution(**precaution) for precaution in plan["precautions"]],
        notes=notes,
    )
