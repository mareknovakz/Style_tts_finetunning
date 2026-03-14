import os
import requests
from huggingface_hub import hf_hub_download
import shutil

# Target directory for StyleTTS2 within the project
BASE_DIR = "StyleTTS2"

# Define weights and their sources in mychen76/styletts2
WEIGHTS = [
    {
        "name": "epoch_00080.pth",
        "repo": "mychen76/styletts2",
        "repo_path": "Utils/ASR/epoch_00080.pth",
        "local_path": "Utils/ASR/epoch_00080.pth"
    },
    {
        "name": "bst.t7",
        "repo": "mychen76/styletts2",
        "repo_path": "Utils/JDC/bst.t7",
        "local_path": "Utils/JDC/bst.t7"
    },
    {
        "name": "config.yml",
        "repo": "mychen76/styletts2",
        "repo_path": "Utils/PLBERT/config.yml",
        "local_path": "Utils/PLBERT/config.yml"
    },
    {
        "name": "step_1000000.t7",
        "repo": "mychen76/styletts2",
        "repo_path": "Utils/PLBERT/step_1000000.t7",
        "local_path": "Utils/PLBERT/step_1000000.t7"
    },
    {
        "name": "epochs_2nd_00020.pth",
        "repo": "mychen76/styletts2",
        "repo_path": "Models/LibriTTS/epochs_2nd_00020.pth",
        "local_path": "Models/LibriTTS/epochs_2nd_00020.pth"
    }
]

def download_weights():
    for weight in WEIGHTS:
        target_path = os.path.join(BASE_DIR, weight["local_path"])
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        print(f"Downloading {weight['name']} from {weight['repo']}...")
        try:
            downloaded_path = hf_hub_download(
                repo_id=weight["repo"],
                filename=weight["repo_path"],
                local_dir=os.path.dirname(target_path),
                local_dir_use_symlinks=False
            )
            # Ensure it's in the exact local_path (sometimes hf_hub_download nests it)
            if os.path.basename(downloaded_path) != os.path.basename(target_path):
                 shutil.move(downloaded_path, target_path)
            
            # Check size
            size = os.path.getsize(target_path)
            if size < 1000:
                print(f"WARNING: {weight['name']} seems too small ({size} bytes). Might be corrupt.")
            else:
                print(f"Successfully downloaded {weight['name']} ({size / (1024*1024):.2f} MB)")
                
        except Exception as e:
            print(f"Error downloading {weight['name']}: {e}")

if __name__ == "__main__":
    download_weights()
