from math import trunc, log10
from random import randrange


def print_matrix(m):
    def max_abs_element(matrix):
        maximum = float('-inf')
        for i in range(0, n):
            for j in range(0, n):
                maximum = max(maximum, abs(matrix[i][j]))
        return maximum

    def count_digits(value):
        return trunc(log10(value)) + 1

    n = len(m)
    digits = count_digits(max_abs_element(m)) + 2
    format_string = f"{{:{digits}}}"

    for i in range(0, n):
        for j in range(0, n):
            print(format_string.format(m[i][j]), end='')
        print('\n')


def generate_square_matrix(n):
    matrix = []
    for i in range(0, n):
        matrix.append([])
        for j in range(0, n):
            matrix[i].append(randrange(- 100, 100))

    return matrix
