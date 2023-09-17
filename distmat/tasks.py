import ray

@ray.remote
def dot_calc(A, B, i, j, k):
    return A.data[i][k] * B.data[k][j]

@ray.remote
def get_submatrix_task(start_row, start_col, order, data):
        from matrix import Matrix
        submatrix = []

        for row in range(order):
            submatrix.append(
                data[start_row + row][start_col:start_col + order])
            
        return submatrix