import ray

@ray.remote
def dot_calc(A, B, i, j, k):
    return A.data[i][k] * B.data[k][j]