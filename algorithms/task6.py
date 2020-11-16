from matrix_utils import generate_square_matrix, print_matrix

def matrix_det(m):

    n = len(m)

    if n == 2:
        return m[0][0] * m[1][1] - m[1][0] * m[0][1]

    sum_det = 0

    for j in range(0, n):
        sub_matrix = m[1:]
        sub_matrix = [list[0:j] + list[j + 1:] for list in sub_matrix]
        sum_det += ((-1) ** (j + 2)) * m[0][j] * matrix_det(sub_matrix)

    return sum_det


if __name__ == '__main__':
    matrix = generate_square_matrix(5)
    print_matrix(matrix)
    print(f"det(A)={matrix_det(matrix)}")
