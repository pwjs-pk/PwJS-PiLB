from os.path import splitext, join
from os import listdir
import re


def assign_temporary_labels(word_dict: dict):
    temp_labels = {}
    for key, value in word_dict.items():
        if key in word_dict.values():
            hashed = str(abs(hash(key)))
            temp_labels[hashed] = value
            word_dict[key] = hashed

    return word_dict, temp_labels


def replace_word(word_dict, string):

    word_dict, temp_labels = assign_temporary_labels(word_dict)

    for word, replacement in word_dict.items():
        regex = re.compile('\\b' + word + '\\b')
        string = re.sub(regex, replacement, string)

    for word, replacement in temp_labels.items():
        regex = re.compile('\\b' + word + '\\b')
        string = re.sub(regex, replacement, string)
    return string


def get_all_files(directory, extension):
    return [(directory, file) for file in listdir(directory) if splitext(file)[1] == extension]


if __name__ == '__main__':
    files = get_all_files('./samples', '.txt')
    new_content = None
    for directory, file in files:
        with open(join(directory, file), 'r') as f:
            content = f.read()
            new_content = replace_word({'i': 'oraz', 'oraz': 'i', 'nigdy': 'prawie nigdy', 'dlaczego': 'czemu'}, content)

        with open(join(directory, 'replaced_' + file), 'w') as f:
            f.write(new_content)
