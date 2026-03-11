# StyleTTS2 Czech Finetuning Repository

This repository is designed for finetuning StyleTTS2 on Czech speech data, specifically optimized for the `classla/ParlaSpeech-CZ` dataset.

## Structure
- `setup.sh`: Installation script for system and python dependencies.
- `prepare_data.py`: Script to download/stream the ParlaSpeech-CZ dataset and prepare it for StyleTTS2.
- `train_cz.py`: Wrapper script to start the finetuning process.
- `Configs/config_ft_cz.yml`: Configuration for the finetuning (Second stage).
- `Data/`: Directory where processed audio and transcriptions will be stored.
- `Models/`: Directory for saved checkpoints.

## Getting Started
1. Run `./setup.sh` to install dependencies.
2. Prepare your data by running `python3 prepare_data.py`.
3. Start finetuning with `python3 train_cz.py`.

## RunPod Instructions
1. Clone this repo to your RunPod instance.
2. Ensure you have a GPU with CUDA support.
3. Run `setup.sh` and proceed with data preparation and training.

## Note on Pretrained Models
Make sure to place the following models in the `StyleTTS2/Models/LibriTTS/` and `StyleTTS2/Utils/` directories as specified in the config:
- Base LibriTTS model
- ASR checkpoint
- JDC (F0) model
- PL-BERT model
