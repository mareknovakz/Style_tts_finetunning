from huggingface_hub import HfApi, list_repo_files
import os

api = HfApi()
# More comprehensive list of potential repos
repos = [
    'yl4579/StyleTTS2-LibriTTS',
    'yl4579/StyleTTS2-LJSpeech',
    'yl4579/StyleTTS2-LibriTTS_v2',
    'amphion/StyleTTS2',
    'burchim/StyleTTS2-Vocos',
    'facebook/wav2vec2-base-960h' # Possible source for ASR component
]

print("\n--- Model Weights Search ---")
for repo_id in repos:
    print(f"\nChecking {repo_id}:")
    try:
        files = list_repo_files(repo_id)
        for f in sorted(files):
            # Case-insensitive check for key model names
            fl = f.lower()
            if "joint_v2.pth" in fl or "bst.t7" in fl or "pytorch_model.bin" in fl or "epochs_2nd" in fl or "checkpoint" in fl:
                print(f"  [FOUND] {f}")
    except Exception as e:
        print(f"  Error: {e}")
