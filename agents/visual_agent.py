# Visual Analysis Agent
from preprocessing.frame_extractor import extract_frames
from models.heuristics import frame_difference_score

class VisualAgent:
    def analyze(self, media):
        print("👁️ Visual Agent: Performing real video analysis")

        frames = extract_frames(media["path"])
        diff_score = frame_difference_score(frames)

        if diff_score > 25:
            return {
                "agent": "VisualAgent",
                "verdict": "FAKE",
                "confidence": min(diff_score / 50, 1.0),
                "reason": "High frame-to-frame inconsistency detected"
            }

        return {
            "agent": "VisualAgent",
            "verdict": "REAL",
            "confidence": 0.6,
            "reason": "Temporal consistency within normal range"
        }
def analyze_video(media):
    agent = VisualAgent()
    return agent.analyze(media)
