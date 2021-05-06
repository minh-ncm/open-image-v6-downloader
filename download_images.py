import pandas as pd

import sys
import getopt
import requests
import os


try:
    opts, args = getopt.getopt(sys.argv[1:],
                               shortopts='ho:a:',
                               longopts=['help=', 'out-path=', 'amount='])
except getopt.GetoptError as e:
    print('use -h or --help for usage info')


OUT_DIR = ''
AMOUNT = 50

for opt, arg in opts:
    if opt in ['-h', '--help']:
        print('usage: python download_images.py [options]')
        print('options:')
        print('-o, --out-path\tdirectory where download images will be save into. Default is in working directory')
        print('-a, --amount\tamount of image will be download, use `all` to download all images. Default is `50`')
        sys.exit()
    elif opt in ['-o', '--output']:
        OUT_DIR = arg
    elif opt in ['-a', '--amount']:
        AMOUNT = arg

IMG_INFO = 'csv/train/simpler-train-images-boxable-with-rotation.csv'
ANNO_INFO = 'csv/train/simpler-oidv6-train-annotations-bbox.csv'
image_urls = pd.read_csv(IMG_INFO)
image_annotations = pd.read_csv(ANNO_INFO)
if AMOUNT == 'all':
    AMOUNT = image_urls.shape[0]

DATA_DIR = os.path.join(OUT_DIR, 'dataset/train')
IMG_DIR = os.path.join(DATA_DIR, 'images')
ANNO_DIR = os.path.join(DATA_DIR, 'annotations')
os.makedirs(IMG_DIR, exist_ok=True)
os.makedirs(ANNO_DIR, exist_ok=True)

short_anno_df = pd.DataFrame()
for i in range(1, int(AMOUNT) + 1):
    # Download images
    image_id = image_urls['ImageID'].loc[i]
    response = requests.get(image_urls['OriginalURL'].loc[i])
    file_name = os.path.join(IMG_DIR, f"{image_id}.jpg")
    file = open(file_name, 'wb')
    file.write(response.content)
    file.close()

    # Create annotations
    short_anno_df = short_anno_df.append(
        image_annotations.loc[image_annotations['ImageID'] == image_id],
        ignore_index=True)
    short_anno_df.columns = image_annotations.columns
    short_anno_df.to_csv(os.path.join(ANNO_DIR, image_id + '.csv'),
                         index=False)

