from download_images import download_images, download_by_classes

import getopt
import sys
import os


# Remove below code if as kaggle utility scripts.
if __name__ == "__main__":
    out_dir = ''
    in_dir = ''
    amount = 50
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   shortopts='ho:a:i:c:',
                                   longopts=[
                                       'help',
                                       'out-path=',
                                       'amount=',
                                       'in-path=',
                                       'classes=',
                                   ])
    except getopt.GetoptError as e:
        # print(e.msg)
        print('use -h or --help for usage info')
        sys.exit()

    is_by_class = False
    classes = []
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('usage: python download_images.py [options]')
            print('options:')
            print('-o, --out-path\tdirectory where download images will be save into. Default is in working directory')
            print('-i, --in-path\tdirectory where the dataset is placed. Default is in working directory.')
            print('-a, --amount\tamount of image will be download, use `all` to download all images. Default is `50`.')
            print('-c, --classes\tlist of classes if you what to categorized dataset by classes, if class is a multi-word use `-` between them. E.g: -c human-face apple')
            sys.exit()
        elif opt in ['-o', '--output']:
            out_dir = arg
        elif opt in ['-a', '--amount']:
            amount = arg
        elif opt in ['-i', '--in-path']:
            in_dir = arg
        elif opt in ['-c', '--classes']:
            classes.append(arg)
            for a in args:
                if a[0] != '-':
                    classes.append(a)
                    break
            is_by_class = True

    # print(out_dir, in_dir, amount, classes)
    if is_by_class:
        result = []
        for class_name in classes:
            class_name = class_name[0].upper() + class_name[1:].lower()
            parts = class_name.split('-')
            class_name = ' '.join(parts)
            result.append(class_name)
        classes = result
        download_by_classes(classes, in_dir=in_dir, out_dir=out_dir)
    else:
        download_images(in_dir=in_dir, out_dir=out_dir, amount=amount)
