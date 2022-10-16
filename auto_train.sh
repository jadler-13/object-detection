#!/bin/bash

# download face mask dataset and install required packages
sh setup.sh

# convert data to correct format, split into training and validation sets and move files to expected directories
python prepare_data.py

# train YOLOv5s model on face mask data
python yolov5/train.py --img 640 --batch 16 --epochs 80 --data facemasks.yaml --weights yolov5s.pt
