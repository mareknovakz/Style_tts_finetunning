#!/bin/bash
# Setup script for StyleTTS2 Czech Finetuning

echo "Setting up StyleTTS2 Czech Finetuning environment..."

# 1. Update and install system dependencies
sudo apt-get update
sudo apt-get install -y espeak-ng git-lfs

# 2. Clone the original StyleTTS2 if it doesn't exist (as a submodule or reference)
if [ ! -d "StyleTTS2" ]; then
    echo "Cloning StyleTTS2 repository..."
    git clone https://github.com/yl4579/StyleTTS2.git
fi

# 3. Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# 4. Install Python dependencies
pip install --upgrade pip
pip install torch torchaudio --index-url https://download.pytorch.org/whl/cu121
pip install munch pyyaml nltk phonemizer librosa click einops transformers accelerate
pip install tensorboard git+https://github.com/resemble-ai/vocos.git
pip install datasets # For ParlaSpeech-CZ

# 5. Download model dependencies if needed
echo "Downloading base models..."
# (Actual download commands will be added here or in a separate script)

echo "Setup complete. Please run: source .venv/bin/activate"
