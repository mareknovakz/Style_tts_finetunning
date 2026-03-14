from huggingface_hub import HfApi
import sys

api = HfApi()
repos = ['yl4579/StyleTTS2-LibriTTS', 'yl4579/StyleTTS2-LJSpeech']

for repo in repos:
    print(f"\n--- Files in {repo} ---")
    try:
        # Use list_repo_tree for recursive listing
        for f in api.list_repo_tree(repo, recursive=True):
            print(f.rfilename)
    except Exception as e:
        print(f"Error listing {repo}: {e}")
