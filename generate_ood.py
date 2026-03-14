import os
import datasets
from datasets import load_dataset
from tqdm import tqdm
import argparse

def generate_ood(output_dir="Data", num_sentences=500):
    os.makedirs(output_dir, exist_ok=True)
    ood_path = os.path.join(output_dir, "OOD_texts.txt")
    
    print(f"Generating OOD texts from classla/ParlaSpeech-CZ (skipping first 50k)...")
    ood_texts = []
    
    try:
        # Load dataset and explicitly disable decoding for the audio column
        dataset = load_dataset("classla/ParlaSpeech-CZ", split="train", streaming=True)
        dataset = dataset.cast_column("audio", datasets.Audio(decode=False))
        # Now remove it to be extra safe
        dataset = dataset.remove_columns(["audio"])
        dataset = dataset.with_format("python")
        
        # Skip a large chunk (50,000) to ensure these sentences are not in the top 10k usually used for training
        dataset = dataset.skip(50000)
        
        for item in tqdm(dataset.take(num_sentences)):
            text = item['text'].strip()
            if text and len(text) > 20:
                ood_texts.append(text)
                
    except Exception as e:
        print(f"Error fetching from dataset: {e}")
        print("Falling back to minimal test set.")
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
