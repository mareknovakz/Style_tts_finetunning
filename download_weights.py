import os
import subprocess
import shutil

# Target directory for StyleTTS2 within the project
BASE_DIR = "StyleTTS2"

# Define weights and their direct resolve URLs from mychen76/styletts2
WEIGHTS = [
    {
        "name": "epoch_00080.pth",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Utils/ASR/epoch_00080.pth",
        "local_path": "Utils/ASR/epoch_00080.pth"
    },
    {
        "name": "bst.t7",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Utils/JDC/bst.t7",
        "local_path": "Utils/JDC/bst.t7"
    },
    {
        "name": "config.yml",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Utils/PLBERT/config.yml",
        "local_path": "Utils/PLBERT/config.yml"
    },
    {
        "name": "step_1000000.t7",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Utils/PLBERT/step_1000000.t7",
        "local_path": "Utils/PLBERT/step_1000000.t7"
    },
    {
        "name": "epochs_2nd_00020.pth",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Models/LibriTTS/epochs_2nd_00020.pth",
        "local_path": "Models/LibriTTS/epochs_2nd_00020.pth"
    },
    {
        "name": "ASR_config.yml",
        "url": "https://huggingface.co/mychen76/styletts2/resolve/main/Utils/ASR/config.yml",
        "local_path": "Utils/ASR/config.yml"
    }
]

def download_weights():
    for weight in WEIGHTS:
        target_path = os.path.join(BASE_DIR, weight["local_path"])
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        print(f"Downloading {weight['name']}...")
        try:
            # Use wget for reliability with HF LFS resolve URLs
            cmd = ["wget", "-q", "--show-progress", weight["url"], "-O", target_path]
            subprocess.run(cmd, check=True)
            
            # Check size
            size = os.path.getsize(target_path)
            if size < 500:
                print(f"WARNING: {weight['name']} seems too small ({size} bytes). Might be corrupt.")
            else:
                print(f"Successfully downloaded {weight['name']} ({size / (1024*1024):.2f} MB)")
                
        except Exception as e:
            print(f"Error downloading {weight['name']}: {e}")

if __name__ == "__main__":
    download_weights()
