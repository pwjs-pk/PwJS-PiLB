from matrix_utils import generate_square_matrix


def matrix_sum(m1, m2):
    if len(m1) != len(m2) and len(m1[0]) != len(m2[0]):
        raise ArithmeticError('matrices have different dimensions!')
    res = []
    n = len(m1)
    for i in range(0, n):
        res.append([])
        for j in range(0, n):
            res[i].append(m1[i][j] + m2[i][j])
    return res


if __name__ == '__main__':
    matrix1 = generate_square_matrix(128)
    matrix2 = generate_square_matrix(128)
    result = matrix_sum(matrix1, matrix2)

