import os
import re

files_to_patch = [
    "models.py",
    "Utils/PLBERT/util.py"
]

def patch_file(filepath):
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (not found)")
        return
    
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Regex to find torch.load(args) and add weights_only=False if not already there
    # We want to match torch.load(...)
    # and insert , weights_only=False before the closing )
    # This is slightly tricky if there are nested parens, but torch.load usually has simple calls here.
    
    # Simplified approach: find torch.load calls and append the parameter
    def replacement(match):
        original = match.group(0)
        if 'weights_only' in original:
            return original
        # Insert before the last )
        return original[:-1] + ", weights_only=False)"

    new_content = re.sub(r'torch\.load\([^)]+\)', replacement, content)
    
    if new_content != content:
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Patched {filepath}")
    else:
        print(f"No changes needed for {filepath}")

if __name__ == "__main__":
    # Assuming we are in StyleTTS2 directory
    for f in files_to_patch:
        patch_file(f)
