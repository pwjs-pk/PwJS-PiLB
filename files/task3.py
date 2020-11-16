from PIL import Image
from os.path import splitext, join
from os import listdir


def convert_to_png(path):
    image = Image.open(path)
    image.save(f"{splitext(path)[0]}.png")


def get_all_files(directory, extension):
    return [join(directory, file) for file in listdir(directory) if splitext(file)[1] == extension]


if __name__ == '__main__':
    files = get_all_files('./images', '.jpg')
    for file in files:
        convert_to_png(file)
