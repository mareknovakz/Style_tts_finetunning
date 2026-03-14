from huggingface_hub import HfApi
import os

api = HfApi()
repo = 'mychen76/styletts2'

def check_sizes():
    print(f"Checking sizes in {repo}...")
    try:
        # list_repo_tree is better for sizes
        for f in api.list_repo_tree(repo_id=repo, recursive=True):
            if hasattr(f, 'size') and f.size is not None:
                if 'bst.t7' in f.path or 'epoch_00080.pth' in f.path or 'pytorch_model.bin' in f.path:
                    print(f"{f.path}: {f.size / (1024*1024):.2f} MB")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_sizes()
