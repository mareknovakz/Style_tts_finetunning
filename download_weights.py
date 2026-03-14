from huggingface_hub import hf_hub_download
import os

repos = [
    "yl4579/StyleTTS2-LibriTTS",
    "TandemApp/StyleTTS2",
    "mishtal/StyleTTS2",
    "yl4579/StyleTTS2-LJSpeech"
]

files_mapping = {
    "joint_v2.pth": ["Utils/ASR/checkpoints/joint_v2.pth", "ASR/checkpoints/joint_v2.pth", "Utils/ASR/checkpoints/joint_v2.pth"],
    "bst.t7": ["Utils/JDC/bst.t7", "JDC/bst.t7"],
    "pytorch_model.bin": ["Utils/PLBERT/pytorch_model.bin", "PLBERT/pytorch_model.bin"],
    "config.yml": ["Utils/PLBERT/config.yml", "PLBERT/config.yml"],
    "epochs_2nd_00020.pth": ["Models/LibriTTS/epochs_2nd_00020.pth", "epochs_2nd_00020.pth"]
}

# The target paths in StyleTTS2 structure
targets = {
    "joint_v2.pth": "Utils/ASR/checkpoints/joint_v2.pth",
    "bst.t7": "Utils/JDC/bst.t7",
    "pytorch_model.bin": "Utils/PLBERT/pytorch_model.bin",
    "config.yml": "Utils/PLBERT/config.yml",
    "epochs_2nd_00020.pth": "Models/LibriTTS/epochs_2nd_00020.pth"
}

def download():
    # If run from parent, go into StyleTTS2
    if os.path.exists("StyleTTS2"):
        os.chdir("StyleTTS2")
        
    for key, target_local in targets.items():
        if os.path.exists(target_local) and os.path.getsize(target_local) > 1000:
            print(f"Skipping {key}, already exists and seems valid.")
            continue
            
        success = False
        for repo in repos:
            for remote_path in files_mapping.get(key, []):
                print(f"Trying to download {key} from {repo} at {remote_path}...")
                try:
                    os.makedirs(os.path.dirname(target_local), exist_ok=True)
                    # Use local_dir="." to avoid cache issues in this context
                    path = hf_hub_download(repo_id=repo, filename=remote_path, local_dir=".", local_dir_use_symlinks=False)
                    
                    # Normalize paths for comparison
                    norm_remote = os.path.normpath(remote_path)
                    norm_target = os.path.normpath(target_local)
                    
                    if norm_remote != norm_target:
                        if os.path.exists(norm_target): os.remove(norm_target)
                        os.makedirs(os.path.dirname(norm_target), exist_ok=True)
                        os.rename(norm_remote, norm_target)
                        # clean up empty parent dirs
                        curr = os.path.dirname(norm_remote)
                        while curr and curr != ".":
                            if not os.listdir(curr):
                                os.rmdir(curr)
                                curr = os.path.dirname(curr)
                            else:
                                break
                    print(f"Successfully downloaded {key}!")
                    success = True
                    break
                except Exception as e:
                    # print(f"  Attempt failed: {e}")
                    continue
            if success: break
        if not success:
            print(f"CRITICAL: FAILED to download {key} from all sources.")

if __name__ == "__main__":
    download()
