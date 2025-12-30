🛡️ DeepGuard-X

Agentic Edge-AI System for Real-Time Deepfake Detection
Team: CodeNova

📌 Project Overview

DeepGuard-X is a proof-of-concept (POC) agentic AI system designed to demonstrate confidence-based deepfake risk assessment in real-world, low-connectivity environments.

The system focuses on on-device decision logic, where detection signals are combined and translated into explainable risk levels, enabling secure and timely responses without relying on cloud infrastructure.

🎯 Objectives

Build an autonomous, agentic decision engine for deepfake risk assessment

Demonstrate confidence-based alerting instead of binary real/fake outputs

Showcase edge-first feasibility suitable for mobile and field deployment

Emphasize explainability, trust, and operational usability

⚙️ Proof of Concept Description

This POC demonstrates:

Simulated detection signal analysis

Weighted confidence score generation (0–100%)

Risk classification into LOW / MEDIUM / HIGH categories

Automated output logging for audit and review

⚠️ Note:
The included video file is used as sample media input for demonstrating pipeline execution.
Full frame-level deepfake detection is out of scope for this prototype.

🧠 Agentic Decision Logic

Based on the generated confidence score:

High Confidence (>85%) → High-Risk Alert

Medium Confidence (60–85%) → Flag for Human Review

Low Confidence (<60%) → Warning Only

This enables adaptive system behavior under uncertainty.

🛠️ Technology Stack

Language: Python

Execution: On-device / local runtime

Libraries: OpenCV, NumPy

Platform: Windows (POC), Edge-deployable design
