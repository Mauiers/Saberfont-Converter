import os


if __name__ == '__main__':
    # open paths.txt and set lines == every line in the file
    with open('paths.txt') as f:
        paths = f.readlines()

    # for each path gathered from paths.txt
    for path in paths:
        # make sure CFX folder exists
        if 'CFX' not in os.listdir(path):
            print('CFX folder not found in ', path)
            continue

        # gather all files within CFX folder

        # copy CFX files into Verso folder

        # rename Verso files to proper format

