from huggingface_hub import hf_hub_download
import os

repo = "yl4579/StyleTTS2-LibriTTS"
files = [
    "ASR/checkpoints/joint_v2.pth",
    "JDC/bst.t7",
    "PLBERT/pytorch_model.bin",
    "PLBERT/config.yml",
    "Models/LibriTTS/epochs_2nd_00020.pth"
]

def download():
    # If run from parent, go into StyleTTS2
    if os.path.exists("StyleTTS2"):
        os.chdir("StyleTTS2")
        
    for f in files:
        print(f"Downloading {f}...")
        # hf_hub_download with local_dir="." will preserve the folder structure from the repo
        # but the repo has ASR/ at root, we want Utils/ASR/
        # So we download to a temp dir and move, or just download to the right place.
        
        # Mapping:
        # ASR/ -> Utils/ASR/
        # JDC/ -> Utils/JDC/
        # PLBERT/ -> Utils/PLBERT/
        
        target_path = f
        if f.startswith("ASR/"):
            target_path = os.path.join("Utils", f)
        elif f.startswith("JDC/"):
            target_path = os.path.join("Utils", f)
        elif f.startswith("PLBERT/"):
            target_path = os.path.join("Utils", f)
            
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        
        # We download and then move to target_path because local_dir preserves the 'f' structure
        downloaded_path = hf_hub_download(repo_id=repo, filename=f, local_dir=".", local_dir_use_symlinks=False)
        
        # If the downloaded path is not the target path, move it
        if f != target_path:
             if os.path.exists(target_path):
                 os.remove(target_path)
             os.rename(f, target_path)
             # Clean up empty parent dir if f was in a subdir
             parent = os.path.dirname(f)
             if parent and not os.listdir(parent):
                 os.rmdir(parent)
        
    print("Download complete.")

if __name__ == "__main__":
    download()
