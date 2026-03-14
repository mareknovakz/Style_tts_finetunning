import os

def patch_file(filepath, replacements):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    new_content = content
    for old, new in replacements.items():
        new_content = new_content.replace(old, new)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Patched {filepath}")
    else:
        print(f"No changes needed for {filepath}")

if __name__ == "__main__":
    patch_file("models.py", {
        "torch.load(path, map_location='cpu')": "torch.load(path, map_location='cpu', weights_only=False)",
        "torch.load(model_path, map_location='cpu')": "torch.load(model_path, map_location='cpu', weights_only=False)"
    })
    
    patch_file("Utils/PLBERT/util.py", {
        "torch.load(log_dir + \"/step_\" + str(iters) + \".t7\", map_location='cpu')": "torch.load(log_dir + \"/step_\" + str(iters) + \".t7\", map_location='cpu', weights_only=False)"
    })
