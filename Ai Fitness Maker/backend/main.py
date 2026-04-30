from __future__ import annotations

from datetime import datetime
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from .pose_rules import analyze_pose
from .recommender import bmi_status, calculate_bmi, recommend_plan
from .schemas import (
    PoseFeedback,
    PoseFrameInput,
    RecommendationResponse,
    UserProfile,
    UserProfileCreate,
    WorkoutSession,
    WorkoutSessionCreate,
    WorkoutSessionUpdate,
)

app = FastAPI(
    title="AI Fitness Maker API",
    version="0.1.0",
    description="Backend scaffold for personalized fitness planning and pose-feedback workflows.",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

USER_STORE: dict[str, UserProfile] = {}
SESSION_STORE: dict[str, WorkoutSession] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/profiles", response_model=UserProfile)
def create_profile(payload: UserProfileCreate) -> UserProfile:
    bmi = calculate_bmi(payload.weight_kg, payload.height_cm)
    profile = UserProfile(
        **payload.model_dump(),
        bmi=bmi,
        bmi_status=bmi_status(bmi),
        daily_calories=round(payload.weight_kg * {"lose": 26, "gain": 34, "maintain": 30}[payload.goal]),
        created_at=datetime.utcnow(),
    )
    USER_STORE[payload.name.lower()] = profile
    return profile


@app.get("/profiles/{user_name}", response_model=UserProfile)
def get_profile(user_name: str) -> UserProfile:
    profile = USER_STORE.get(user_name.lower())
    if profile is None:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@app.post("/recommendations", response_model=RecommendationResponse)
def build_recommendation(payload: UserProfileCreate) -> RecommendationResponse:
    return recommend_plan(payload)


@app.post("/pose/analyze", response_model=PoseFeedback)
def analyze_pose_frame(payload: PoseFrameInput) -> PoseFeedback:
    return analyze_pose(payload.detector_id, payload.landmarks)


@app.post("/sessions", response_model=WorkoutSession)
def create_session(payload: WorkoutSessionCreate) -> WorkoutSession:
    session = WorkoutSession(
        session_id=str(uuid4()),
        user_name=payload.user_name,
        exercise_name=payload.exercise_name,
        goal=payload.goal,
        reps_completed=0,
        correct_reps=0,
        wrong_pose_events=0,
        duration_seconds=0,
        created_at=datetime.utcnow(),
    )
    SESSION_STORE[session.session_id] = session
    return session


@app.patch("/sessions/{session_id}", response_model=WorkoutSession)
def update_session(session_id: str, payload: WorkoutSessionUpdate) -> WorkoutSession:
    session = SESSION_STORE.get(session_id)
    if session is None:
        raise HTTPException(status_code=404, detail="Session not found")

    updated = session.model_copy(
        update={
            "reps_completed": payload.reps_completed,
            "correct_reps": payload.correct_reps,
            "wrong_pose_events": payload.wrong_pose_events,
            "duration_seconds": payload.duration_seconds,
        }
    )
    SESSION_STORE[session_id] = updated
    return updated


@app.get("/sessions", response_model=list[WorkoutSession])
def list_sessions() -> list[WorkoutSession]:
    return list(SESSION_STORE.values())
