import os

def patch_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    with open(filename, 'r') as f:
        content = f.read()
    
    # Add missing imports if not present
    prefix = "import os\nimport os.path as osp\n"
    if "import os.path as osp" not in content:
        content = prefix + content
        print(f"Added imports to {filename}")
    
    # Add try-except for main()
    # Handle different styles of __main__ block
    if 'if __name__=="__main__":' in content:
        content = content.replace('if __name__=="__main__":', 'if __name__ == "__main__":')
    
    old_main = 'if __name__ == "__main__":\n    main()'
    new_main = 'if __name__ == "__main__":\n    try:\n        main()\n    except Exception as e:\n        import traceback\n        traceback.print_exc()\n        raise e'
    
    if old_main in content:
        content = content.replace(old_main, new_main)
        print(f"Patched main in {filename}")
    else:
        print(f"Could not find main block in {filename} or already patched")

    with open(filename, 'w') as f:
        f.write(content)

if __name__ == "__main__":
    # If run from parent, go into StyleTTS2
    if os.path.exists("StyleTTS2"):
        os.chdir("StyleTTS2")
    patch_file("train_finetune.py")
    patch_file("train_finetune_accelerate.py")
