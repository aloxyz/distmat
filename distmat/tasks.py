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

@ray.remote
def inv_cof_matrix(A, row, cols):
    from matrix import Matrix
    
    cof_row = []
    minor_futures = [Matrix.dist_minor.remote(A, row, col) for col in range(cols)]
    minors = ray.get(minor_futures)

    for col,minor in zip(range(cols), minors):
        cof_row.append(((-1)**(row + col)) * minor.det())

    return cof_row

@ray.remote
def inv_calc(row, cof_cols, cof_data, det):
    for col in range(cof_cols):
        return (row, col, (cof_data[row][col] / det))