# Entry point for DeepGuard-X
from agents.ingestion_agent import IngestionAgent
from agents.visual_agent import VisualAgent
from agents.sync_agent import SyncAgent
from agents.decision_agent import DecisionAgent

def main():
    print("🚀 DeepGuard-X starting...")

    ingestion = IngestionAgent()
    visual = VisualAgent()
    sync = SyncAgent()
    decision = DecisionAgent()

    media_path = "data/samples/sample.mp4"

    media = ingestion.load(media_path)

    visual_result = visual.analyze(media)
    sync_result = sync.analyze(media)

    final_decision = decision.decide(
        visual_result,
        sync_result
    )

    print("\n🛡️ FINAL RESULT")
    print(final_decision)

if __name__ == "__main__":
    main()
