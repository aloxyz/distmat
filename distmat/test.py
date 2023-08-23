
from matrix import Matrix
import numpy as np

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
    
    # A = Matrix.random(5, 5, 0, 99)
    # print(A)

    # b = Matrix.random(1, 5, 0, 99)
    # print(b)
    # print(Matrix.dot(b,b))

    elements = [12,42,63,94,215]
    A = Matrix(elements)

    print(A.get_elements())
    print("numpy: ", np.dot(np.array(elements), np.array(elements)))
    print("distmat: ", Matrix.dot(A, A))


if __name__ == "__main__":
    main()

