#!/bin/bash
# runpod_init.sh - Download mandatory weights for StyleTTS2

mkdir -p StyleTTS2/Utils/ASR/checkpoints
mkdir -p StyleTTS2/Utils/JDC
mkdir -p StyleTTS2/Utils/PLBERT
mkdir -p StyleTTS2/Models/LibriTTS

echo "Downloading ASR checkpoints..."
wget -O StyleTTS2/Utils/ASR/checkpoints/joint_v2.pth https://huggingface.co/yl4579/StyleTTS2-LibriTTS/resolve/main/Utils/ASR/checkpoints/joint_v2.pth

echo "Downloading JDC (F0) model..."
wget -O StyleTTS2/Utils/JDC/bst.t7 https://huggingface.co/yl4579/StyleTTS2-LibriTTS/resolve/main/Utils/JDC/bst.t7

echo "Downloading PL-BERT model..."
wget -O StyleTTS2/Utils/PLBERT/config.yml https://huggingface.co/yl4579/StyleTTS2-LibriTTS/resolve/main/Utils/PLBERT/config.yml
wget -O StyleTTS2/Utils/PLBERT/pytorch_model.bin https://huggingface.co/yl4579/StyleTTS2-LibriTTS/resolve/main/Utils/PLBERT/pytorch_model.bin

echo "Downloading Base LibriTTS model (2nd stage)..."
wget -O StyleTTS2/Models/LibriTTS/epochs_2nd_00020.pth https://huggingface.co/yl4579/StyleTTS2-LibriTTS/resolve/main/Models/LibriTTS/epochs_2nd_00020.pth

echo "Weights download complete."
