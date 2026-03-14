import os
import sys

def patch_file(filename):
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Add missing imports
    prefix = ""
    if filename.endswith(".py") and "import os.path as osp" not in content:
        prefix += "import os\nimport os.path as osp\n"
        
    if filename == "utils.py" and "matplotlib.use" not in content:
        prefix = "import matplotlib\nmatplotlib.use('Agg')\n" + prefix
        
    if prefix:
        content = prefix + content
        print(f"Added imports to {filename}")
    
    # 2. Disable warning suppression
    content = content.replace("warnings.simplefilter('ignore')", "pass # warnings.simplefilter('ignore')")
    
    # 3. Add checkpoints to main()
    content = content.replace('    config = yaml.safe_load(open(config_path))', 
                             '    print("--- [CHECKPOINT: Config Load] ---")\n    config = yaml.safe_load(open(config_path))\n    print("--- [CHECKPOINT: Config Success] ---")')

    # 4. Normalize __main__ block and add diagnostic info
    if 'if __name__ == "__main__":' in content or 'if __name__=="__main__":' in content:
        # Simple string replacement for normalization
        content = content.replace('if __name__=="__main__":', 'if __name__ == "__main__":')
        parts = content.split('if __name__ == "__main__":')
        if len(parts) > 1:
            new_tail = (
                'if __name__ == "__main__":\n'
                '    import nltk\n'
                '    import sys\n'
                '    try:\n'
                '        print("--- [NLTK DOWNLOAD] ---")\n'
                '        nltk.download("punkt")\n'
                '        nltk.download("punkt_tab")\n'
                '    except Exception as ne: print(f"NLTK failure: {ne}")\n'
                '    try:\n'
                '        print(f"--- [STARTING MAIN] Argv: {sys.argv} ---")\n'
                '        main()\n'
                '    except Exception as e:\n'
                '        print(f"--- [CRASHED IN MAIN]: {e} ---")\n'
                '        import traceback\n'
                '        traceback.print_exc()\n'
                '        sys.exit(1)\n'
            )
            content = parts[0] + new_tail

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == "__main__":
    if os.path.exists("StyleTTS2"):
        os.chdir("StyleTTS2")
    for f in ["train_finetune.py", "train_finetune_accelerate.py", "utils.py", "models.py"]:
        patch_file(f)
    print("Repair complete.")
