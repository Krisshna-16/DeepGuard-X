# Streamlit demo UI
# ui/streamlit_app.py
import streamlit as st
import sys
import os

# Ensure project root is in Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Import agents
from agents.ingestion_agent import ingest_media
from agents.visual_agent import analyze_video
from agents.sync_agent import analyze_audio_sync
from agents.decision_agent import make_final_decision

st.set_page_config(page_title="🛡️ DeepGuard-X", layout="wide")
st.title("🛡️ DeepGuard-X")
st.write("Agentic Deepfake Detection System")

# Upload area
uploaded_file = st.file_uploader("Upload Video", type=["mp4"])

if uploaded_file:
    st.video(uploaded_file)  # Preview the uploaded video

    if st.button("Analyze Video"):
        st.info("Analyzing video, please wait...")

        # Step 1: Ingest the uploaded file
        media_data = ingest_media(uploaded_file)

        # Step 2: Run Visual Agent
        visual_result = analyze_video(media_data)
        st.subheader("👁️ Visual Agent Output")
        st.json(visual_result)

        # Step 3: Run Sync Agent
        sync_result = analyze_audio_sync(media_data)
        st.subheader("🎵 Sync Agent Output")
        st.json(sync_result)

        # Step 4: Run Decision Agent
        final_result = make_final_decision(visual_result, sync_result)
        verdict = final_result["final_verdict"]

        st.subheader("🧠 Final Verdict")
        if verdict.lower() == "fake":
            st.error("⚠️ Deepfake Detected!")
        else:
            st.success("✅ Video Seems Real")

        # Step 5: Show risk and explanation
        st.write("Risk Level:", final_result["risk"])
        st.write("Explanation:")
        for reason in final_result["explanation"]:
            st.write("-", reason)
