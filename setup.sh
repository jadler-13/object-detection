#!/bin/bash

# clone YOLOv5 repo and install required packages
git clone https://github.com/ultralytics/yolov5
pip install -r yolov5/requirements.txt -q
pip install pylabel -q
pip install kaggle -q
sudo apt install unzip -q

# create kaggle API token to enable dataset download
mkdir ~/.kaggle
touch ~/.kaggle/kaggle.json
echo '{"username":"your_username","key":"your_key}' > ~/.kaggle/kaggle.json
chmod 600 ~/.kaggle/kaggle.json

# download & unzip facemask dataset
kaggle datasets download -d andrewmvd/face-mask-detection -q
unzip face-mask-detection.zip -d facemask_data -q
