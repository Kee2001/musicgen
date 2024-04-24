#!/bin/bash
# Let's call this script venv.sh

brew install python@3.9

brew install ffmpeg
brew install virtualenv
rm -rf ./venv/audiocraft
python3.9 -m venv ./venv/audiocraft
source ./venv/audiocraft/bin/activate

pip install setuptools wheel
pip install -U demucs==4.0.1 
pip install basic-pitch==0.3.3
pip install torch==2.1.0
pip install -U audiocraft==1.2.0
pip install tensorboard==2.16.2
