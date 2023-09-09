
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random_int(4, 4, -99, 99)
    b = Matrix.random_float(4, 4, -99, 99)

    # DOT PRODUCT
    print("\ndistmat:\n", Matrix.dot(a,b))
    print("numpy: \n", np.dot(np.array(a.get()), np.array(b.get())))

    # INVERSE
    print("\ndistmat:\n", a.inv())
    print("numpy: \n", np.linalg.inv(np.array(a.get())))

    # DETERMINANT
    print("numpy: ", np.linalg.det(np.array(a.get())))
    print("distmat: ", a.det())

    # RANK
    print("numpy: ", np.linalg.matrix_rank(np.array(a.get())))
    print("distmat: ", a.rank())


if __name__ == "__main__":
    main()

