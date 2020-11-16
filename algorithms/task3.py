def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ArithmeticError('vector lengths should match!')
    return sum([el[0] * el[1] for el in zip(v1, v2)])


if __name__ == '__main__':
    a = [1, 2, 12, 4]
    b = [2, 4, 2, 8]
    print(dot_product(a, b))
