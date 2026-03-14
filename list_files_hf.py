from huggingface_hub import HfApi
import sys

api = HfApi()
repos = [
    'yl4579/StyleTTS2-LibriTTS',
    'TandemApp/StyleTTS2',
    'OedoSoldier/StyleTTS2',
    'mishtal/StyleTTS2'
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
            
            if name and any(x in name.lower() for x in ["joint_v2.pth", "bst.t7", "pytorch_model.bin", "epochs_2nd"]):
                print(f"  [FOUND] {name}")
    except Exception as e:
        print(f"  Error: {e}")
