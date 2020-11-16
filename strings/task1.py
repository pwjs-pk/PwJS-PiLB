from os.path import splitext, join
from os import listdir
import re


def remove_word(word_list, string):
    for word in word_list:
        regex = re.compile('\\b' + word + '\\b')
        string = re.sub(regex, '', string)
    return string


def get_all_files(directory, extension):
    return [(directory, file) for file in listdir(directory) if splitext(file)[1] == extension]


if __name__ == '__main__':
    files = get_all_files('./samples', '.txt')
    new_content = None
    for directory, file in files:
        with open(join(directory, file), 'r') as f:
            content = f.read()
            new_content = remove_word(['się', 'i', 'oraz', 'nigdy', 'dlaczego'], content)

        with open(join(directory, 'removed_' + file), 'w') as f:
            f.write(new_content)
