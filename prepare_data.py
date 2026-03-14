import torch
from datasets import load_dataset
import os
import phonemizer
from tqdm import tqdm
import argparse
import soundfile as sf

# Dataset: classla/ParlaSpeech-CZ
# Format: wav|phonemes|speaker_id

import torch
import datasets
from datasets import load_dataset
import os
import phonemizer
from tqdm import tqdm
import argparse
import soundfile as sf
import io
import librosa
import numpy as np

# Dataset: classla/ParlaSpeech-CZ
# Format: wav|phonemes|speaker_id

def prepare_data(output_dir="Data", max_samples=0, split="train"):
    os.makedirs(output_dir, exist_ok=True)
    wavs_dir = os.path.join(output_dir, "wavs")
    os.makedirs(wavs_dir, exist_ok=True)
    
    print(f"Loading dataset classla/ParlaSpeech-CZ (split: {split})...")
    # Load dataset and explicitly disable decoding for the audio column
    dataset = load_dataset("classla/ParlaSpeech-CZ", split=split, streaming=True)
    dataset = dataset.cast_column("audio", datasets.Audio(decode=False))
    dataset = dataset.with_format("python")
    
    # Initialize phonemizer
    global_phonemizer = phonemizer.backend.EspeakBackend(language='cs', preserve_punctuation=True, with_stress=True)

    train_list = []
    val_list = []
    
    count = 0
    print(f"Preparing samples (max: {max_samples if max_samples > 0 else 'all'})...")
    
    for item in tqdm(dataset):
        if max_samples > 0 and count >= max_samples:
            break
            
        audio_data = item['audio']
        text = item['text']
        speaker_id = item.get('speaker_id', item.get('speaker_info', {}).get('speaker_id', 'unknown'))
        
        # Save audio
        wav_filename = f"sample_{count:06d}.wav"
        wav_path = os.path.join(wavs_dir, wav_filename)
        
        if not os.path.exists(wav_path):
            try:
                # Load from bytes using librosa/soundfile to be safe
                if isinstance(audio_data, dict) and 'bytes' in audio_data and audio_data['bytes']:
                    audio_bytes = audio_data['bytes']
                    with io.BytesIO(audio_bytes) as f:
                        y, sr = librosa.load(f, sr=24000) # Target SR for StyleTTS2
                        sf.write(wav_path, y, sr)
                elif isinstance(audio_data, dict) and 'path' in audio_data:
                    # If it's a local path or similar
                    y, sr = librosa.load(audio_data['path'], sr=24000)
                    sf.write(wav_path, y, sr)
                else:
                    # Fallback to whatever 'audio' object is if it was decoded anyway
                    # but since we set decode=False, it should be bytes
                    continue
            except Exception as e:
                print(f"Error processing audio for sample {count}: {e}")
                continue
        
        # Phonemize
        try:
            phonemes = global_phonemizer.phonemize([text])[0]
        except Exception as e:
            print(f"Error phonemizing sample {count}: {e}")
            continue
        
        # Append to list
        line = f"{wav_filename}|{phonemes}|{speaker_id}"
        
        if count % 20 != 0:
            train_list.append(line)
        else:
            val_list.append(line)
        
        count += 1
        if count % 100 == 0:
            with open(os.path.join(output_dir, f"train_list_partial.txt"), "w", encoding="utf-8") as f:
                f.write("\n".join(train_list))

    with open(os.path.join(output_dir, "train_list.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(train_list))
    
    with open(os.path.join(output_dir, "val_list.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(val_list))

    print(f"Data preparation complete. Total samples: {count}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Prepare ParlaSpeech-CZ for StyleTTS2")
    parser.add_argument("--output_dir", type=str, default="Data", help="Output directory")
    parser.add_argument("--max_samples", type=int, default=100, help="Maximum samples to process (0 for all)")
    parser.add_argument("--split", type=str, default="train", help="Dataset split (train/validation/test)")
    
    args = parser.parse_args()
    prepare_data(output_dir=args.output_dir, max_samples=args.max_samples, split=args.split)
