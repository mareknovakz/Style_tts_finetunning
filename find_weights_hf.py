from huggingface_hub import HfApi
import os

api = HfApi()

def find_files():
    print("Searching for yl4579 models...")
    models = api.list_models(author='yl4579')
    for model in models:
        # Check files in each model
        # Note: list_repo_files for models
        try:
            files = api.list_repo_files(repo_id=model.modelId)
            for file in files:
                if 'joint_v2.pth' in file or 'bst.t7' in file:
                    print(f"FOUND {file} in {model.modelId}")
        except:
            pass

if __name__ == "__main__":
    find_files()
