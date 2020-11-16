from matrix_utils import generate_square_matrix, print_matrix


def multiply_matrices(m1, m2):
    n = len(m1)
    result = []
    for i in range(0, n):
        result.append([])
        for j in range(0, n):
            total = 0
            for r in range(0, n):
                total += m1[i][r] * m2[r][j]
            result[i].append(total)

    return result


if __name__ == '__main__':
    matrix1 = generate_square_matrix(8)
    matrix2 = generate_square_matrix(8)
    res = multiply_matrices(matrix1, matrix2)
    print_matrix(res)
