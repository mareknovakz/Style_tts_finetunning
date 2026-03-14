from huggingface_hub import HfApi
import os

api = HfApi()

def find_files():
    print("Searching for StyleTTS2 related models...")
    models = api.list_models(search='StyleTTS2')
    count = 0
    for model in models:
        count += 1
        if count > 20: break
        print(f"Checking {model.modelId}...")
        try:
            files = api.list_repo_files(repo_id=model.modelId)
            for file in files:
                if 'joint_v2.pth' in file or 'bst.t7' in file:
                    print(f"  [FOUND] {file} in {model.modelId}")
        except:
            pass

if __name__ == "__main__":
    find_files()
