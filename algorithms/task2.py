from random import randrange


def quicksort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quicksort(array, p, q - 1)
        quicksort(array, q + 1, r)


def partition(array, p, r):
    x = array[r]
    i = p - 1
    for j in range(p, r):
        if array[j] >= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i + 1]
    return i + 1


def generate_random(n):
    rands = []
    for i in range(0, n):
        rands.append(randrange(-100, 100))
    return rands


def verify(array):
    is_valid = True

    for i in range(0, len(array) - 1):
        if array[i + 1] > array[i]:
            is_valid = False
            break

    return is_valid


if __name__ == '__main__':
    tab = generate_random(50)
    print(f"is sorted before quicksort: {verify(tab)}")
    quicksort(tab, 0, len(tab) - 1)
    print(tab)
    print(f"is sorted after quicksort: {verify(tab)}")
