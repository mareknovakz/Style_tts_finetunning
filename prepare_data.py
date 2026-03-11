import torch
from datasets import load_dataset
import os
import phonemizer
from tqdm import tqdm

# Dataset: classla/ParlaSpeech-CZ
# Format: wav|phonemes|speaker_id

def prepare_data(output_dir="Data"):
    os.makedirs(output_dir, exist_ok=True)
    
    print("Loading dataset classla/ParlaSpeech-CZ...")
    # Loading just a sample for testing as requested
    dataset = load_dataset("classla/ParlaSpeech-CZ", split="train", streaming=True)
    
    # Initialize phonemizer
    global_phonemizer = phonemizer.backend.EspeakBackend(language='cs', preserve_punctuation=True, with_stress=True)

    train_list = []
    val_list = []
    
    count = 0
    max_count = 100 # For testing, we'll take 100 samples
    
    print(f"Preparing {max_count} samples...")
    for item in tqdm(dataset.take(max_count)):
        audio = item['audio']
        text = item['text']
        speaker_id = item.get('speaker_id', '0')
        
        # Save audio
        wav_filename = f"sample_{count}.wav"
        wav_path = os.path.join(output_dir, "wavs", wav_filename)
        os.makedirs(os.path.dirname(wav_path), exist_ok=True)
        
        # Audio is a dict with 'array' and 'sampling_rate'
        import soundfile as sf
        sf.write(wav_path, audio['array'], audio['sampling_rate'])
        
        # Phonemize
        phonemes = global_phonemizer.phonemize([text])[0]
        
        # Append to list
        line = f"{wav_filename}|{phonemes}|{speaker_id}"
        if count < 90:
            train_list.append(line)
        else:
            val_list.append(line)
        
        count += 1

    with open(os.path.join(output_dir, "train_list.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(train_list))
    
    with open(os.path.join(output_dir, "val_list.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(val_list))

    print("Data preparation complete.")

if __name__ == "__main__":
    prepare_data()
