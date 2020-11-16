from os import listdir
from os.path import isfile, join


def count_files(directory):
    return len([file for file in listdir(directory) if isfile(join(directory, file))])


if __name__ == '__main__':
    path = '/dev'
    print(f"Files in {path}: {count_files(path)}")
