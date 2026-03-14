import os
from datasets import load_dataset
from tqdm import tqdm
import argparse

def generate_ood(output_dir="Data", num_sentences=500):
    os.makedirs(output_dir, exist_ok=True)
    ood_path = os.path.join(output_dir, "OOD_texts.txt")
    
    print(f"Generating OOD texts from local source...")
    ood_texts = []
    
    # Try to find a local Czech text file to use as OOD
    local_source = "../War and peace A2.txt"
    if os.path.exists(local_source):
        with open(local_source, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # Take a middle chunk to get different sentences
            start = len(lines) // 4
            for line in lines[start:]:
                clean_line = line.strip()
                if clean_line and len(clean_line) > 20: # Ensure it's a decent sentence
                    ood_texts.append(clean_line)
                    if len(ood_texts) >= num_sentences:
                        break
    
    if not ood_texts:
        # Extreme fallback
        ood_texts = ["Toto je testovací věta pro StyleTTS2.", "Příprava dat probíhá úspěšně.", "Czech language is beautiful."] * (num_sentences // 3 + 1)

    with open(ood_path, "w", encoding="utf-8") as f:
        f.write("\n".join(ood_texts[:num_sentences]))
        
    print(f"OOD texts generated at {ood_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate OOD texts for StyleTTS2")
    parser.add_argument("--output_dir", type=str, default="Data", help="Output directory")
    parser.add_argument("--num_sentences", type=int, default=500, help="Number of sentences to generate")
    
    args = parser.parse_args()
    generate_ood(output_dir=args.output_dir, num_sentences=args.num_sentences)
