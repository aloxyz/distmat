def get_submatrices_rank(matrix, order):
    for m in matrix.get_square_submatrices(order):
        if m.det() != 0:
            return order

    return -1
