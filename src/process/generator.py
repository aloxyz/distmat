import random

def generate_matrix(rows, cols):
    mat = [[random.randint(0, 99) for _ in range(cols)] for _ in range(rows)]
    return mat
