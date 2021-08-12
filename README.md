# About
This module main purpose is for downloading google open image v6 dataset. <br>
But use this [dataset](https://www.kaggle.com/tarantula3/google-open-image-v6) 
which is a smaller dataset of the [original](https://opensource.google/projects/open-images-dataset). <br>
The smaller one contain image's urls, label names, human-verified annotations 
in csv files. <br>

# Usage
First you need to have the smaller dataset downloaded. (or you can add the 
dataset to your notebook if you work on kaggle.) <br>
run `python main.py -h` for help

Example:
- Change downloaded dataset output directory: <br>
`python main.py -o C:/users/output`
- Select where the input dataset is downloaded: <br> 
`python main.py -i C:/user/download`

## Download some images and all its annotations
Example: <br> 
- Download 10 images: <br>
`python main.py -a 10` <br>

## Download images and create annotations by classes
Example: <br>
- Download training dataset for __Apple__ and __Polar bear__: <br>
`python main.py -c polar-bear apple`

# TODO
- Fix some minor issues in my dataset.
- create script for downloading test dataset.