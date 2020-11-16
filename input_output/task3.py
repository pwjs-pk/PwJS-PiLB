def get_key(message):
    key = None
    while key is None:
        key = input(message)
    return key


if __name__ == '__main__':
    original_key = get_key('Pass original key: ')
    new_key = get_key('Pass key: ')

    if original_key == new_key:
        print('Keys are matched')
    else:
        print('Keys are different')
