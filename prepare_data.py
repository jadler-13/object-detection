# this script converts the Kaggle dataset "Face Mask Detection" from PascalVOC to YOLO format, 
# splits it into training and validation sets, and moves all files to the directories expected by YOLOv5;

import os
import random
from pylabel import importer
from shutil import move

# define some file paths for later use
path = os.getcwd()
data = path+'/facemask_data'
annotations = data+'/annotations/'
images = data+'/images/'

# convert data from PascalVOC to YOLO format using PyLabel
old_labels = importer.ImportVOC(annotations)
labels = old_labels.export.ExportToYoloV5()

# path to new labels created by PyLabel
labels = path+'/training/labels/'

# randomly select 20% of image indexes for validation set
num_images = len(os.listdir(images))
valid_idx = random.sample(range(0, num_images-1), round(num_images*0.2))

# create directories for images and new labels where YOLOv5 expects them
images_train = images+'training/'
images_valid = images+'validation/'
os.mkdir(images_train)
os.mkdir(images_valid)
labelpath = data+'/labels/'
labels_train = labelpath+'training/'
labels_valid = labelpath+'validation/'
os.mkdir(labelpath)
os.mkdir(labels_train)
os.mkdir(labels_valid)

# move images and labels to new directories, split into training and validation sets
for index in range(num_images):
    image = f'maksssksksss{index}.png'
    label = f'maksssksksss{index}.txt'
    if index in valid_idx:
        move(images+image, images_valid+image)
        move(labels+label, labels_valid+label)
    else:
        move(images+image, images_train+image)
        move(labels+label, labels_train+label)

# verify that image and label numbers in new directories are as expected
print(f'images in validation set: {len(os.listdir(images_valid))}\nimages in training set: {len(os.listdir(images_train))}')
print(f'labels in validation set: {len(os.listdir(labels_valid))}\nlabels in training set: {len(os.listdir(labels_train))}')

# read class names from .yaml file created by PyLabel
classes = []
with open(path+'/training/dataset.yaml', 'r') as file:
    for line in file:
        if '-' in line:
            content = line.split()
            if content[1] == 'mask_weared_incorrect': classes.append('mask_worn_incorrectly')
            else: classes.append(content[1])
print(f'\nclasses: {classes}')

# write new .yaml file in the format and directory expected by YOLOv5
with open(path+'/yolov5/data/facemasks.yaml', 'w') as file:
    file.write(f"path: {data}\n")
    file.write("train: images/training\n")
    file.write("val: images/validation\n")
    file.write(f"\nnames:\n  0: {classes[0]}\n  1: {classes[1]}\n  2: {classes[2]}")
