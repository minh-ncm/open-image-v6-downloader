import os
from PIL import Image


def delete_corrupted_images(img_file):
    try:
        image = Image.open(img_file)
        image.verify()
        image.close()
        return False
    except IOError as e:
        os.remove(img_file)
        return True
