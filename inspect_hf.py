from huggingface_hub import HfApi, list_repo_files
import sys

api = HfApi()
print("\n--- Searching for StyleTTS2 repositories ---")
try:
    repos = api.list_models(search="StyleTTS2")
    for r in repos[:30]:
        print(f"Repo: {r.repo_id}")
        try:
            files = list_repo_files(r.repo_id)
            for f in files:
                if "joint_v2.pth" in f:
                    print(f"  FOUND ASR: {f} in {r.repo_id}")
                if "bst.t7" in f:
                    print(f"  FOUND JDC: {f} in {r.repo_id}")
                if "pytorch_model.bin" in f and "PLBERT" in f:
                    print(f"  FOUND PLBERT: {f} in {r.repo_id}")
        except:
            continue
except Exception as e:
    print(f"Error: {e}")
