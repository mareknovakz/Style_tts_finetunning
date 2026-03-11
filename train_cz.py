import os
import sys
import yaml
import shutil

# This script is a wrapper to start finetuning
# It ensures the StyleTTS2 codebase is accessible and paths are correct

def train():
    # 1. Path setup
    base_dir = os.path.dirname(os.path.abspath(__file__))
    styletts2_dir = os.path.join(base_dir, "StyleTTS2")
    
    if not os.path.exists(styletts2_dir):
        print("StyleTTS2 directory not found. Did you run setup.sh?")
        return

    # Add StyleTTS2 to path
    sys.path.append(styletts2_dir)
    sys.path.append(os.path.join(styletts2_dir, "Modules"))
    
    # 2. Run training
    # We'll call the main function from StyleTTS2/train_finetune.py
    # But since it's a click command, we'll run it via os.system or subprocess
    # for simplicity in this wrapper, but let's try to import it first
    
    config_path = os.path.join(base_dir, "Configs/config_ft_cz.yml")
    
    # We'll use the original train_finetune.py but override it with our config
    cmd = f"cd {styletts2_dir} && python3 train_finetune.py --config_path {config_path}"
    
    print(f"Executing: {cmd}")
    os.system(cmd)

if __name__ == "__main__":
    train()
