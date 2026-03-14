from huggingface_hub import HfApi
import os

api = HfApi()
repo = 'mychen76/styletts2'

def list_files():
    print(f"Listing files in {repo}...")
    try:
        files = api.list_repo_files(repo_id=repo)
        for f in sorted(files):
            print(f)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    list_files()
