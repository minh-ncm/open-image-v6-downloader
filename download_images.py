import pandas as pd

import sys
import getopt
import requests
import os


def download_images(out_dir='', in_dir='', amount=50):
    in_dir = os.path.join(in_dir, 'csv')
    in_dir = os.path.join(in_dir, 'train')
    img_info = os.path.join(in_dir, 'simpler-train-images-boxable-with-rotation.csv')
    anno_info = os.path.join(in_dir, 'simpler-oidv6-train-annotations-bbox.csv')

    image_urls = pd.read_csv(img_info)
    image_annotations = pd.read_csv(anno_info)
    if amount == 'all':
        amount = image_urls.shape[0]

    data_dir = os.path.join(out_dir, 'dataset/train')
    img_dir = os.path.join(data_dir, 'images')
    anno_dir = os.path.join(data_dir, 'annotations')
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(anno_dir, exist_ok=True)

    short_anno_df = pd.DataFrame()
    for i in range(1, int(amount) + 1):
        # Download images
        image_id = image_urls['ImageID'].loc[i]
        response = requests.get(image_urls['OriginalURL'].loc[i])
        file_name = os.path.join(img_dir, f"{image_id}.jpg")
        file = open(file_name, 'wb')
        file.write(response.content)
        file.close()

        # Create annotations
        short_anno_df = short_anno_df.append(
            image_annotations.loc[image_annotations['ImageID'] == image_id],
            ignore_index=True)
        short_anno_df.columns = image_annotations.columns
        short_anno_df.to_csv(os.path.join(anno_dir, image_id + '.csv'),
                             index=False)


# Remove below code if as kaggle utility scripts.
if __name__ == "__main__":
    out_dir = ''
    in_dir = ''
    amount = 50
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   shortopts='ho:a:i:',
                                   longopts=[
                                       'help=',
                                       'out-path=',
                                       'amount=',
                                       'in-path='
                                   ])
    except getopt.GetoptError as e:
        print('use -h or --help for usage info')

    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('usage: python download_images.py [options]')
            print('options:')
            print('-o, --out-path\tdirectory where download images will be save into. Default is in working directory')
            print('-i, --in-path\tdirectory where the dataset is placed. Default is in working directory.')
            print('-a, --amount\tamount of image will be download, use `all` to download all images. Default is `50`')
            sys.exit()
        elif opt in ['-o', '--output']:
            out_dir = arg
        elif opt in ['-a', '--amount']:
            amount = arg
        elif opt in ['-i', '--in-path']:
            in_dir = arg
    download_images(out_dir, in_dir, amount)
