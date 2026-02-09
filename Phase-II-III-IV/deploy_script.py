import os
from huggingface_hub import HfApi

# Read token
token_path = os.path.expanduser("~/.cache/huggingface/token")
if not os.path.exists(token_path):
     # Fallback for Windows if ~ expansion fails weirdly
     token_path = r"C:\Users\hp\.cache\huggingface\token"

try:
    with open(token_path, "r") as f:
        token = f.read().strip()
except Exception as e:
    print(f"Error reading token: {e}")
    exit(1)

api = HfApi(token=token)
repo_id = "abdullah9873/backend-rag-chatbot-v3"

try:
    print(f"Uploading updated folder 'backend' to {repo_id}...")
    api.upload_folder(
        folder_path="backend",
        repo_id=repo_id,
        repo_type="space",
        path_in_repo=".",
        ignore_patterns=[".venv", "__pycache__", "*.pyc", ".env"]
    )
    print("Deployment successful!")
except Exception as e:
    print(f"Deployment failed: {e}")
    exit(1)