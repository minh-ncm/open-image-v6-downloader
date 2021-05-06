# open-image-v6

## About
The dataset is original from google open image v6 dataset. <br>
You can find more information about the full dataset 
[here](https://opensource.google/projects/open-images-dataset) <br>
But this module use this [dataset](https://www.kaggle.com/tarantula3/google-open-image-v6) 
which is created from the original dataset and only important values(to me, 
at least) to lower storage.

## Usage
First you need to have [this](https://www.kaggle.com/tarantula3/google-open-image-v6) 
downloaded. (or you can add the dataset to your notebook if you work on kaggle.)

### Download some images and all its annotations
download_image.py allow you to specify the amount of images you want to download
and where put the dataset and its annotations after the download<br>
run `python download_images.py -h` for help

## TODO
- create script for downloading only a certain type of class
- create script for downloading test dataset