# Ingestion Agent
# Ingestion Agent
# ingestion_agent.py
import tempfile

# Ingestion Agent class (optional, for organization)
class IngestionAgent:
    def load(self, path):
        print("📥 Ingestion Agent: Loading media")
        return {"path": path}

# Top-level function for Streamlit
def ingest_media(uploaded_file):
    """
    Takes a Streamlit UploadedFile object and writes it to a temporary file.
    Returns a dictionary with the file path for downstream agents.
    """
    # Create a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp_file:
        # Write the uploaded content to temp file
        tmp_file.write(uploaded_file.read())
        tmp_path = tmp_file.name

    # Return as dictionary with "path" key
    return {"path": tmp_path}

