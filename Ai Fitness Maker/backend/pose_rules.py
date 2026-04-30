from __future__ import annotations

from .schemas import PoseFeedback


def analyze_pose(detector_id: str, landmarks: dict[str, float | int]) -> PoseFeedback:
    """
    Lightweight backend rule engine.
    The frontend can send precomputed angles here.
    A trained ML classifier can replace this module later without changing the API contract.
    """
    left_arm = float(landmarks.get("left_arm_angle", 0))
    right_arm = float(landmarks.get("right_arm_angle", 0))
    left_knee = float(landmarks.get("left_knee_angle", 0))
    right_knee = float(landmarks.get("right_knee_angle", 0))
    hip = float(landmarks.get("hip_angle", 0))

    if detector_id == "pushup":
        avg_arm = (left_arm + right_arm) / 2
        if avg_arm < 90:
            if hip < 155:
                return PoseFeedback(rep_increment=0, state="down", feedback="Keep your body straight.", form_ok=False)
            return PoseFeedback(rep_increment=0, state="down", feedback="Good depth. Push up.", form_ok=True)
        if avg_arm > 155:
            return PoseFeedback(rep_increment=1, state="up", feedback="Rep counted. Lower down again.", form_ok=True)
        return PoseFeedback(rep_increment=0, state="transition", feedback="Extend your arms fully.", form_ok=False)

    if detector_id == "squat":
        avg_knee = (left_knee + right_knee) / 2
        if avg_knee < 100:
            if hip < 50:
                return PoseFeedback(rep_increment=0, state="down", feedback="Keep your chest up.", form_ok=False)
            return PoseFeedback(rep_increment=0, state="down", feedback="Good squat depth. Stand up.", form_ok=True)
        if avg_knee > 165:
            return PoseFeedback(rep_increment=1, state="up", feedback="Rep counted. Descend for next squat.", form_ok=True)
        return PoseFeedback(rep_increment=0, state="transition", feedback="Control the movement.", form_ok=True)

    if detector_id == "plank":
        if 155 <= hip <= 195:
            return PoseFeedback(rep_increment=0, state="hold", feedback="Good plank alignment.", form_ok=True)
        if hip < 155:
            return PoseFeedback(rep_increment=0, state="hold", feedback="Raise your hips slightly.", form_ok=False)
        return PoseFeedback(rep_increment=0, state="hold", feedback="Lower your hips slightly.", form_ok=False)

    return PoseFeedback(rep_increment=0, state="unknown", feedback="Detector is active.", form_ok=True)
