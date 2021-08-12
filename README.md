# About
This repo main purpose is for downloading dataset for object detection problem 
from google open image v6 dataset. <br>
The repo use this [files](https://www.kaggle.com/tarantula3/google-open-image-v6) 
which is a simpler csv files of the [original](https://opensource.google/projects/open-images-dataset). <br>
The smaller one contain image's urls, label names, human-verified annotations. 
in csv files. <br>
After download each image's annotations file will contain these: 
<i>ImageID, LabelName, XMin, XMax, YMin, YMax</i><br>

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
<b>NOTE:</b> <i>--amount</i> not yet support for this feature.<br>
Example: <br>
- Download training dataset for __Apple__ and __Polar bear__: <br>
`python main.py -c polar-bear apple`

# TODO
- add to use --amount in download_by_classes function.
- create script for downloading test dataset.
- improve speed.