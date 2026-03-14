from huggingface_hub import HfApi
import sys

api = HfApi()
repos = [
    'yl4579/StyleTTS2-LibriTTS',
    'TandemApp/StyleTTS2',
    'CapybaraStyle/StyleTTS2',
    'mishtal/StyleTTS2',
    'mrfakename/StyleTTS2-LibriTTS'
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
                 # Filter to find weights
                 nl = name.lower()
                 if "joint_v2.pth" in nl or "bst.t7" in nl or "pytorch_model.bin" in nl or "epochs_2nd" in nl:
                     print(f"  [FOUND] {name}")
    except Exception as e:
        print(f"  Error: {e}")
