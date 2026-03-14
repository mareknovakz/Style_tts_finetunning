from huggingface_hub import HfApi
import sys

api = HfApi()
repos = [
    'yl4579/StyleTTS2-LibriTTS',
    'mrfakename/StyleTTS2-LibriTTS',
    'mrfakename/StyleTTS-2-Demo',
    'yl4579/StyleTTS2-LJSpeech'
]

for repo in repos:
    print(f"\n--- Files in {repo} ---")
    try:
        # Use list_repo_tree for recursive listing
        for f in api.list_repo_tree(repo, recursive=True):
            name = None
            if hasattr(f, 'path'):
                name = f.path
            elif hasattr(f, 'rfilename'):
                name = f.rfilename
            
            if name:
                # Print all files to see the structure
                print(f"  {name}")
    except Exception as e:
        print(f"  Error: {e}")
