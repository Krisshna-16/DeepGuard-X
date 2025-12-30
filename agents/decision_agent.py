# Decision Agent
# Decision Agent
class DecisionAgent:
    def decide(self, visual, sync):
        print("🧠 Decision Agent: Resolving agent disagreement")

        if visual["verdict"] != sync["verdict"]:
            return {
                "final_verdict": "FAKE",
                "risk": "HIGH",
                "explanation": [
                    visual["reason"],
                    sync["reason"]
                ]
            }

        return {
            "final_verdict": visual["verdict"],
            "risk": "LOW",
            "explanation": [visual["reason"]]
        }

# Top-level function for Streamlit import
def make_final_decision(visual_result, sync_result):
    agent = DecisionAgent()
    return agent.decide(visual_result, sync_result)

