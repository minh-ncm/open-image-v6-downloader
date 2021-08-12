import os
import requests

import pandas as pd

from utils import delete_corrupted_images


def download_images(in_dir='../input/google-open-image-v6', out_dir='', amount=20):
    """
    Download images and create its annotations from csv files.
    :param out_dir: Directory where to put downloaded data
    :param in_dir: Directory where csv folder is in.
    :param amount: Amount of images for downloading.
    :return:
    """
    in_dir = os.path.join(in_dir, 'csv')
    in_dir = os.path.join(in_dir, 'train')
    img_info = os.path.join(in_dir, 'simpler-train-images-boxable-with-rotation.csv')
    anno_info = os.path.join(in_dir, 'simpler-oidv6-train-annotations-bbox.csv')

    try:
        if not os.path.isfile(img_info):
            raise FileNotFoundError
        if not os.path.isfile(img_info):
            raise FileNotFoundError
    except FileNotFoundError as e:
        print("input file not found.")

    print('Loadding data from csv files.')
    image_urls = pd.read_csv(img_info)
    image_annotations = pd.read_csv(anno_info)
    if amount == 'all':
        amount = image_urls.shape[0]

    data_dir = os.path.join(out_dir, 'dataset/train')
    img_dir = os.path.join(data_dir, 'images')
    anno_dir = os.path.join(data_dir, 'annotations')
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(anno_dir, exist_ok=True)

    print('Downloading images.')
    for i in range(1, int(amount) + 1):
        # Download images
        image_id = image_urls['ImageID'].loc[i]
        response = requests.get(image_urls['OriginalURL'].loc[i])
        file_name = os.path.join(img_dir, f"{image_id}.jpg")
        file = open(file_name, 'wb')
        file.write(response.content)
        file.close()

        # Delete image if corrupted
        if delete_corrupted_images(file_name):
            continue

        # Create annotations
        short_anno_df = pd.DataFrame()
        short_anno_df = short_anno_df.append(
            image_annotations.loc[image_annotations['ImageID'] == image_id],
            ignore_index=True)
        short_anno_df.columns = image_annotations.columns
        short_anno_df.to_csv(os.path.join(anno_dir, image_id + '.csv'),
                             index=False)
    print('Done.')


def download_by_classes(classes, in_dir='', out_dir=''):
    """
    Download images and create its annotations while categorized by classes.
    :param classes: List of classes to be downloaded.
    :param in_dir: Directory where csv folder is in.
    :param out_dir: Directory where to put downloaded data
    :return:
    """
    in_dir = os.path.join(in_dir, 'csv')
    label_csv_path = os.path.join(in_dir, 'class-descriptions-boxable.csv')
    in_dir = os.path.join(in_dir, 'train')
    img_csv_path = os.path.join(in_dir,
                            'simpler-train-images-boxable-with-rotation.csv')
    anno_csv_path = os.path.join(in_dir, 'simpler-oidv6-train-annotations-bbox.csv')

    try:
        if not os.path.isfile(img_csv_path):
            raise FileNotFoundError
        if not os.path.isfile(img_csv_path):
            raise FileNotFoundError
    except FileNotFoundError as e:
        print("input file not found.")

    print('Loading data from csv files.')
    urls_df = pd.read_csv(img_csv_path)
    annotations_df = pd.read_csv(anno_csv_path)
    label_df = pd.read_csv(label_csv_path)

    data_dir = os.path.join(out_dir, 'dataset/train')
    img_dir = os.path.join(data_dir, 'images')
    anno_dir = os.path.join(data_dir, 'annotations')
    os.makedirs(img_dir, exist_ok=True)
    os.makedirs(anno_dir, exist_ok=True)

    for class_name in classes:
        img_class_dir = os.path.join(img_dir, class_name)
        anno_class_dir = os.path.join(anno_dir, class_name)
        os.makedirs(img_class_dir, exist_ok=True)
        os.makedirs(anno_class_dir, exist_ok=True)

        label_ids = label_df[label_df['LabelName'] == class_name]['LabelID']
        annotations = annotations_df[annotations_df['LabelName'].isin(label_ids)]

        images_id = annotations['ImageID']
        images_id = set(images_id)

        print(f'Downloading {class_name}.')
        for im_id in images_id:
            url = urls_df[urls_df['ImageID'] == im_id]['OriginalURL']
            response = requests.get(url.values[0])
            img_file = os.path.join(img_class_dir, f"{im_id}.jpg")
            file = open(img_file, 'wb')
            file.write(response.content)
            file.close()

            # Delete image if corrupted
            if delete_corrupted_images(img_file):
                continue

            image_anno = annotations[annotations['ImageID'] == im_id]
            image_anno.columns = annotations_df.columns
            anno_file = os.path.join(anno_class_dir, f'{im_id}.csv')
            image_anno.to_csv(anno_file, index=False)
        print(f'Finished download {class_name}.')
    print('Done.')
