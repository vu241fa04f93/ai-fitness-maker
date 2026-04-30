# AI Fitness Maker Backend

This backend converts the current HTML prototype into a project with a defendable system architecture.

## What it covers

- User profile creation with BMI and calorie estimation
- Goal-based recommendation API for food, exercise, and precautions
- Pose-analysis endpoint with backend rule logic
- Workout session creation and progress tracking

## Run locally

```bash
pip install -r requirements.txt
uvicorn backend.main:app --reload
```

Open `http://127.0.0.1:8000/docs` for Swagger UI.

## Suggested frontend integration

- On login submit, call `POST /profiles`
- For plan generation, call `POST /recommendations`
- When the user starts an exercise, call `POST /sessions`
- While camera detection runs, send angle data to `POST /pose/analyze`
- Save rep count and pose errors using `PATCH /sessions/{session_id}`

## ML upgrade path

The current pose service is rule-based so the project remains simple to demo. For a stronger final-year project, replace `backend/pose_rules.py` with:

1. MediaPipe or MoveNet landmark extraction
2. Feature engineering from joint angles and temporal movement windows
3. A classifier for pose correctness
4. A rep-state model for start/down/up/complete transitions

Good model options:

- Random Forest for correctness classification
- XGBoost for tabular angle features
- LSTM or 1D CNN for time-series landmark windows

## Recommended database later

If you continue the project, move from in-memory stores to:

- SQLite for demo
- PostgreSQL for full deployment
