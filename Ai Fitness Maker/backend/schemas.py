from __future__ import annotations

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field


Goal = Literal["lose", "gain", "maintain"]
Gender = Literal["male", "female", "other"]


class UserProfileCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    age: int = Field(ge=10, le=100)
    gender: Gender
    height_cm: float = Field(gt=80, le=250)
    weight_kg: float = Field(gt=20, le=350)
    goal: Goal


class UserProfile(UserProfileCreate):
    bmi: float
    bmi_status: str
    daily_calories: int
    created_at: datetime


class Meal(BaseModel):
    time: str
    name: str
    items: list[str]
    calories: int
    protein_g: int
    carbs_g: int
    fat_g: int


class Exercise(BaseModel):
    name: str
    sets: str
    muscle: str
    type: str
    difficulty: str
    detector_id: str


class Precaution(BaseModel):
    title: str
    text: str


class RecommendationResponse(BaseModel):
    bmi: float
    bmi_status: str
    goal: Goal
    daily_calories: int
    meals: list[Meal]
    exercises: list[Exercise]
    precautions: list[Precaution]
    notes: list[str]


class PoseFrameInput(BaseModel):
    detector_id: str
    landmarks: dict[str, float | int]


class PoseFeedback(BaseModel):
    rep_increment: int
    state: str
    feedback: str
    form_ok: bool


class WorkoutSessionCreate(BaseModel):
    user_name: str
    exercise_name: str
    goal: Goal


class WorkoutSessionUpdate(BaseModel):
    reps_completed: int = Field(ge=0)
    correct_reps: int = Field(ge=0)
    wrong_pose_events: int = Field(ge=0)
    duration_seconds: int = Field(ge=0)


class WorkoutSession(BaseModel):
    session_id: str
    user_name: str
    exercise_name: str
    goal: Goal
    reps_completed: int
    correct_reps: int
    wrong_pose_events: int
    duration_seconds: int
    created_at: datetime
