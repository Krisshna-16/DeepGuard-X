# Heuristic detection methods
import cv2
import numpy as np

def frame_difference_score(frames):
    diffs = []

    for i in range(len(frames) - 1):
        gray1 = cv2.cvtColor(frames[i], cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(frames[i + 1], cv2.COLOR_BGR2GRAY)
        diff = np.mean(cv2.absdiff(gray1, gray2))
        diffs.append(diff)

    return np.mean(diffs) if diffs else 0
