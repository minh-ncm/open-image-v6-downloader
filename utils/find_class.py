import getopt
import sys

import pandas as pd


def find_class_available(class_name, in_dir='../'):
    """
    Check if there is a class exist in dataset.
    :param class_name: name of the class need to be checked.
    :param in_dir: directory where the csv files is placed.
    :return: where the class exist or not.
    """
    classes = pd.read_csv(in_dir + 'csv/class-descriptions-boxable.csv')
    classes = classes.drop('LabelID', axis=1)

    return (classes['LabelName'] == class_name).any()


if __name__ == '__main__':
    try:
        opts, args = getopt.getopt(sys.argv[1:],
                                   shortopts='ho:a:i:c:',
                                   longopts=[
                                       'help',
                                       'in-path=',
                                       'class_name=',
                                   ])
    except getopt.GetoptError as e:
        # print(e.msg)
        print('use -h or --help for usage info')
        sys.exit()

    class_name = ''
    in_dir = '../'
    for opt, arg in opts:
        if opt in ['-h', '--help']:
            print('usage: python download_images.py [options]')
            print('options:')
            print('-i, --in-path\tdirectory where the dataset is placed. '
                  'Default is in working directory.')
            print('-c, --class\tname of the class you need to check.')
            sys.exit()
        elif opt in ['-i', '--in-path']:
            in_dir = arg
        elif opt in ['-c', '--class']:
            class_name = arg

    class_name = class_name[0].upper() + class_name[1:].lower()
    parts = class_name.split('-')
    class_name = ' '.join(parts)

    if find_class_available(class_name, in_dir=in_dir):
        print('Found', class_name)
    else:
        print('Not found', class_name)
