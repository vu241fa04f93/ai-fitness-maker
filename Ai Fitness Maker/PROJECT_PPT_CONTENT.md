# AI Fitness Maker PPT Content

Use this structure for your presentation. It directly matches the three rubric points you shared.

## 1. Introduction

Title:
AI Fitness Maker: Personalized Fitness Planning and Real-Time Exercise Monitoring

Problem statement:
- Many users do not know which diet and workout plan matches their body condition.
- Beginners often perform exercises with the wrong posture.
- Existing static fitness websites do not adapt properly to individual body data.

Objective:
- Build a website that collects user details.
- Classify the user condition using BMI and goal selection.
- Generate a personalized food plan, exercise plan, and precautions.
- Monitor exercise posture using camera-based pose detection.
- Count repetitions automatically and warn the user about wrong posture.

## 2. Proposed System

Modules:
- User login/profile module
- BMI and condition analysis module
- Goal selection module
- Personalized plan generation module
- Camera-based pose detection module
- Repetition counting and feedback module
- Session tracking backend

Suggested architecture slide:
- Frontend: HTML, CSS, JavaScript
- Backend: FastAPI/Python
- ML/Computer Vision: MediaPipe landmarks + pose classification logic
- Storage: User profiles and workout sessions

## 3. Frontend Improvements You Should Mention

Your current idea is correct, but improve it at the start like this:

- Separate registration from login
- Add activity level, dietary preference, and medical condition fields
- Add password or secure login if this is treated as a real system
- Show BMI, calorie target, and goal recommendation after profile submission
- Add dashboard cards for daily calories, target weight, completed workouts, and weekly progress
- Add history page to show previous sessions and rep counts
- Add progress charts for weight change and workout consistency
- Add clear warnings for users with obesity, underweight status, or health risks
- Add fallback exercise videos when camera detection is not available

## 4. Backend Design

Explain the backend in simple flow:

1. User submits profile details
2. Backend stores the profile
3. Backend calculates BMI and calorie target
4. Backend generates a personalized plan based on goal
5. Camera module extracts body landmarks
6. Pose analysis checks posture correctness
7. Rep counter updates session results
8. Backend stores workout history for later analysis

Recommended APIs:
- `POST /profiles`
- `POST /recommendations`
- `POST /pose/analyze`
- `POST /sessions`
- `PATCH /sessions/{session_id}`

## 5. ML Model Explanation

Be careful here: your current HTML uses rule-based pose logic, not a trained ML model. In the PPT, present it honestly:

Phase 1:
- MediaPipe Pose detects body landmarks from webcam frames.
- Joint angles are calculated from shoulder, elbow, hip, knee, and ankle points.
- Rules determine whether posture is correct and whether a repetition is completed.

Phase 2 improvement:
- Collect a dataset of correct and incorrect exercise poses
- Train a model to classify pose correctness
- Use time-series landmark sequences for more robust rep counting

Suggested exercises for the dataset:
- Squat
- Push-up
- Plank
- Lunge
- Bicep curl

Possible input features:
- Elbow angle
- Knee angle
- Hip angle
- Shoulder alignment
- Body inclination
- Temporal change between consecutive frames

Possible output classes:
- Correct pose
- Incorrect pose
- Up position
- Down position
- Transition

## 6. Performance Evaluation of the Proposed Model

This is the most important part for your rubric.

For recommendation system:
- BMI classification accuracy
- Plan generation response time
- User satisfaction score from feedback form

For pose detection model/system:
- Pose detection accuracy
- Precision
- Recall
- F1-score
- Rep counting accuracy
- Average inference time per frame
- False warning rate

If you do not have a trained classifier yet, evaluate the system version like this:
- Number of successful detections per total frames
- Correct rep count compared with manual count
- Correct posture warning count compared with manual observation
- Latency in milliseconds

Example result table:

| Exercise | Test Videos | Correct Rep Count | Actual Rep Count | Accuracy |
|---|---:|---:|---:|---:|
| Squat | 10 | 94 | 100 | 94% |
| Push-up | 10 | 91 | 100 | 91% |
| Plank posture check | 10 | 46 correct detections | 50 actual | 92% |

For classification metrics if you train a model:

| Metric | Squat | Push-up | Plank |
|---|---:|---:|---:|
| Precision | 0.93 | 0.91 | 0.95 |
| Recall | 0.90 | 0.89 | 0.94 |
| F1-score | 0.91 | 0.90 | 0.94 |

## 7. Presentation of Results and Discussion

Show results clearly using:
- BMI classification examples for 3 different users
- Screenshots of login page, goal page, plan page, and camera page
- Table of calorie plans for different goals
- Bar chart of rep-count accuracy by exercise
- Line chart of response time or latency
- Confusion matrix if you train a classifier

Discussion points:
- The system successfully personalizes fitness plans based on user profile and goal.
- Real-time pose monitoring improves exercise correctness.
- Rep counting reduces manual effort.
- Rule-based detection works for basic exercises but may fail under poor lighting, occlusion, or side-view angles.
- A trained model and larger dataset can improve robustness.

## 8. Deriving the Conclusions

Use something close to this:

Conclusion:
The AI Fitness Maker website achieved the main objectives of collecting user health data, identifying body condition, generating personalized food and exercise plans, and monitoring exercises through pose detection. The system was able to provide real-time feedback and automatic repetition counting for selected exercises. The project demonstrates that AI-based fitness assistance can improve personalization and workout safety. Future work includes database integration, stronger authentication, mobile support, and a trained pose-classification model for higher accuracy.

## 9. Suggested Final Slide Order

1. Title
2. Problem statement
3. Objectives
4. Existing system limitations
5. Proposed system
6. System architecture
7. Frontend modules
8. Backend modules
9. ML/pose detection workflow
10. Implementation screenshots
11. Performance evaluation metrics
12. Results table and graphs
13. Discussion
14. Conclusion
15. Future scope

## 10. What To Say If Faculty Asks “Where Is The AI?”

Use this answer:

"The AI part of the current prototype is the camera-based pose estimation using body landmarks and intelligent decision logic for posture feedback and repetition counting. In the advanced version, the same pipeline can be extended with a trained classification model on pose sequences for more accurate real-time error detection."
