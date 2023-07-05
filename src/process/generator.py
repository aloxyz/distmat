import random

def generate_matrix(rows, cols):
    mat = []
    print(rows, cols)
    
    for i in range(rows):
        for j in range(cols):
            mat[i][j] = random.randint(0, 99)

    return mat
