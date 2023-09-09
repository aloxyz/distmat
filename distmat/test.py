
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random_int(4, 4, -99, 99)
    b = Matrix.random_float(1, 4, -99, 99)

    # DOT PRODUCT
    # print(Matrix.dot(a,b))
    # print(np.dot(np.array(a.get()), np.array(b.get())))

    # ADDITION
    # print(a + b)
    # print(np.add(a, 4))

    # SUBTRACTIONS
    # print(np.subtract(a, b))
    # print(a - b)

    # INVERSE
    print("\ndistmat:\n", a.inv())
    print("numpy: \n", np.linalg.inv(np.array(a.get())))

    # DETERMINANT
    # print("numpy: ", np.linalg.det(np.array(a.get_data())))
    # print("distmat: ", a.det())

    # RANK
    # print("numpy: ", np.linalg.matrix_rank(np.array(a.get_data())))
    # print("distmat: ", a.rank())


if __name__ == "__main__":
    main()

