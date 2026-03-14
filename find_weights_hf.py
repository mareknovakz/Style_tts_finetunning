from huggingface_hub import HfApi
import os

api = HfApi()

def find_exact_file():
    print("Searching for joint_v2.pth in ALL models...")
    # This might be slow but let's try to find it
    models = api.list_models(search='StyleTTS2')
    for model in models:
        try:
            files = api.list_repo_files(repo_id=model.modelId)
            for f in files:
                if 'joint_v2.pth' in f:
                    print(f"FOUND joint_v2.pth in {model.modelId} at {f}")
        except:
            pass
    
    print("\nSearching for joint_v2.pth in larger search space...")
    # Maybe try 'ASR' or 'Text-Mel'
    models = api.list_models(search='ASR')
    count = 0
    for model in models:
        count += 1
        if count > 50: break
        try:
            files = api.list_repo_files(repo_id=model.modelId)
            for f in files:
                if 'joint_v2.pth' in f:
                    print(f"FOUND joint_v2.pth in {model.modelId} at {f}")
        except:
            pass

if __name__ == "__main__":
    find_exact_file()
