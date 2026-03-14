from huggingface_hub import list_repo_files
import sys

repos = ["yl4579/StyleTTS2", "yl4579/StyleTTS2-LibriTTS"]

for repo in repos:
    print(f"\n--- Files in {repo} ---")
    try:
        files = list_repo_files(repo)
        for f in sorted(files):
            print(f)
    except Exception as e:
        print(f"Error listing {repo}: {e}")
