from math import sqrt
from sys import argv


def square_zeros(a, b, c):
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        raise ValueError('Zeros are complex numbers')

    x1 = ((-b - sqrt(delta)) / (2 * a))
    x2 = ((-b + sqrt(delta)) / (2 * a))

    return x1, x2


def format_output(a, b, c):
    def format_first(v):
        if v == -1:
            return "-x^2"
        elif v == 1:
            return "x^2"
        else:
            return str(v) + "x^2"

    def format_middle(v):
        if v == -1:
            return "-x"
        elif v == 1:
            return "+x"
        elif v == 0:
            return ""
        elif v > 1:
            return "+" + str(v) + "x"
        elif v < 1:
            return str(v) + "x"

    def format_last(v):
        if v > 0:
            return "+" + str(v)
        else:
            return str(v)

    output = 'f(x) = '
    output += format_first(a)
    output += format_middle(b)
    output += format_last(c)
    output += ' : '

    return output


if __name__ == '__main__':
    a = int(argv[1])
    b = int(argv[2])
    c = int(argv[3])

    print(format_output(a, b, c) + str(square_zeros(a, b, c)))

