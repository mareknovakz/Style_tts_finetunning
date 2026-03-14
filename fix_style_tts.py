import os

def patch_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Add missing imports if not present
    prefix = ""
    if filename.endswith(".py") and "import os.path as osp" not in content:
        prefix += "import os\nimport os.path as osp\n"
        
    if filename == "utils.py" and "matplotlib.use" not in content:
        prefix = "import matplotlib\nmatplotlib.use('Agg')\n" + prefix
        
    if prefix:
        content = prefix + content
        print(f"Added imports to {filename}")
    
    # Add try-except for main()
    # Normalize __main__ block
    content = content.replace('if __name__=="__main__":', 'if __name__ == "__main__":')
    content = content.replace('if __name__ == "__main__" :', 'if __name__ == "__main__":')
    
    old_main = 'if __name__ == "__main__":\n    main()'
    new_main = 'if __name__ == "__main__":\n    try:\n        print("--- [STARTING MAIN] ---")\n        main()\n    except Exception as e:\n        import traceback\n        traceback.print_exc()\n        raise e'
    
    if old_main in content:
        content = content.replace(old_main, new_main)
        print(f"Patched main in {filename}")

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if os.path.exists("StyleTTS2"):
        os.chdir("StyleTTS2")
    patch_file("train_finetune.py")
    patch_file("train_finetune_accelerate.py")
    patch_file("utils.py")
    patch_file("models.py")
    print("Repair complete.")
