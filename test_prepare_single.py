import os
import soundfile as sf
import phonemizer
from tqdm import tqdm

# Mock test for single sample finetuning preparation
# This uses the Krysař sample as a "user provided" file test

def test_prepare_single():
    output_dir = "Data"
    os.makedirs(output_dir, exist_ok=True)
    os.makedirs(os.path.join(output_dir, "wavs"), exist_ok=True)
    
    # Path to the sample we identified earlier
    sample_src = "/home/marek/LibriVox_3/inference/styletts2_test/krysar_2007_librivox_krysar_01_dyk_128kb_seg_0000.wav"
    sample_dst = os.path.join(output_dir, "wavs", "test_sample.wav")
    
    if os.path.exists(sample_src):
        import shutil
        shutil.copy(sample_src, sample_dst)
        text = "Viktor Dyk. Krysař."
    else:
        print("Source sample not found. Generating a dummy wav.")
        import numpy as np
        data = np.random.uniform(-1, 1, 48000)
        sf.write(sample_dst, data, 24000)
        text = "Pokusný text pro test."

    # Phonemize
    backend = phonemizer.backend.EspeakBackend(language='cs', preserve_punctuation=True, with_stress=True)
    phonemes = backend.phonemize([text])[0]
    
    # Create lists
    line = f"test_sample.wav|{phonemes}|0"
    
    with open(os.path.join(output_dir, "train_list.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    
    with open(os.path.join(output_dir, "val_list.txt"), "w", encoding="utf-8") as f:
        f.write(line)
        
    print(f"Prepared test sample with text: {text}")
    print(f"Phonemes: {phonemes}")

if __name__ == "__main__":
    test_prepare_single()
