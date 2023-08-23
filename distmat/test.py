
from matrix import Matrix
import numpy as np

def main():
    # A = Matrix.random(5, 5, -99, 99)
    # print(A)

    # b = Matrix.random(1, 8, -99, 99)
    # print(b)

    # c = Matrix.random(8, 1, -99, 99)
    # print(c)

    # print(Matrix.dot(b,c))

    elements = [12,42,63,94,215]
    A = Matrix(elements)

    print(A.get_elements(), A.transpose().get_elements())
    print("numpy: ", np.dot(np.array(elements), np.array(elements)))
    print("distmat: ", Matrix.dot(A, A.transpose()))


if __name__ == "__main__":
    main()

