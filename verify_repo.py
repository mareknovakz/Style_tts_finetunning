import os
import yaml

def verify_repo(config_path="Configs/config_ft_cz.yml"):
    if not os.path.exists(config_path):
        print(f"ERROR: Config file not found at {config_path}")
        return False
        
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
        
    # Paths to check
    paths_to_verify = [
        config.get('ASR_path'),
        config.get('F0_path'),
        config.get('PLBERT_dir'),
        config.get('pretrained_model'),
        config.get('data_params', {}).get('train_data'),
        config.get('data_params', {}).get('val_data'),
        config.get('data_params', {}).get('OOD_data'),
    ]
    
    # Flatten if any are dirs/lists
    all_fine = True
    print("\n--- StyleTTS2 Readiness Check ---")
    
    # Check StyleTTS2 submodule
    if not os.path.exists("StyleTTS2"):
        print("[-] StyleTTS2 submodule/directory: MISSING")
        all_fine = False
    else:
        print("[+] StyleTTS2 submodule/directory: FOUND")

    for path in paths_to_verify:
        if not path:
            continue
            
        if os.path.exists(path):
            print(f"[+] {path}: FOUND")
        else:
            print(f"[-] {path}: MISSING")
            all_fine = False
            
    print("---------------------------------")
    if all_fine:
        print("SUCCESS: All mandatory files and configurations are present.")
    else:
        print("WARNING: Some files are missing. Training may fail.")
        
    return all_fine

if __name__ == "__main__":
    verify_repo()
