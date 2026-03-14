from huggingface_hub import list_repo_files
import sys

repo = "yl4579/StyleTTS2-LJSpeech"
print(f"\n--- Files in {repo} ---")
try:
    files = list_repo_files(repo)
    found = False
    for f in sorted(files):
        if "joint_v2.pth" in f or "bst.t7" in f:
            print(f"  [FOUND] {f}")
            found = True
    if not found:
        print("  No relevant files found in this repo.")
except Exception as e:
    print(f"Error: {e}")
