from os import listdir
from os.path import isfile, isdir, join


def list_files(path, recursive=True):
    files = [file for file in listdir(path) if isfile(join(path, file))]
    dirs = [directory for directory in listdir(path) if isdir(join(path, directory))]

    for file in files:
        print(join(path, file))

    if recursive:
        for directory in dirs:
            list_files(join(path, directory))


if __name__ == '__main__':
    list_files('/dev')
