from huggingface_hub import HfApi
import os

api = HfApi()
repo = 'mychen76/styletts2'

def check_all_sizes():
    print(f"Checking ALL sizes in {repo}...")
    try:
        for f in api.list_repo_tree(repo_id=repo, recursive=True):
            if hasattr(f, 'size') and f.size is not None:
                print(f"{f.path}: {f.size / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_all_sizes()
