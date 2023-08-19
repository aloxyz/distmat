
from matrix import Matrix
import numpy as np
import random

def main():
    A = Matrix([
        [4, 0, 2, 6],
        [8, 9, 1, 3],
        [5, 8, 4, 1],
        [6, 3, 0, 2]
    ])


    # print(np.linalg.det(np.array(elements)))
    # print(B.det())

    # print(Matrix(np.linalg.inv(np.array(elements))))
    # print(B.inv().transpose())

    # print(Matrix(np.dot(np.array(elements))))
    # print(B.inv().transpose())

    A_elements = [[random.randint(0, 99) for _ in range(5)] for _ in range(5)]
    b_elements = [[random.randint(0, 99)] for _ in range(5)]
    
    A = Matrix(A_elements)
    print(A, A.transpose())

    b = Matrix(b_elements)

    print(b, b.transpose())

    # print(Matrix.dot(B,B))


if __name__ == "__main__":
    main()

