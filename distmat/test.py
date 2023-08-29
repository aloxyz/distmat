
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random_int(3, 3, -99, 99)
    b = Matrix.random_float(3, 1, -99, 99)

    # DOT PRODUCT
    # print(f"{a}*\n{b}=\n{Matrix.dot(a,b)}")
    # print(a, Matrix.dot(a, 2))
    # print(Matrix.dot(a, b))
    # print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))

    # OUTER PRODUCT
    # print(f"{a}*\n{b}=\n{Matrix.outer_product(a,b)}")
    # print(np.outer(np.array(a.get_elements()), np.array(b.get_elements())))

    # ADDITION
    # print(a,b)
    # print(Matrix.add(a, b))

    # INVERSE
    # print("\ndistmat:\n", a.inv())
    # print("numpy: \n", np.linalg.inv(np.array(a.get_elements())))

    # DETERMINANT
    # print("numpy: ", np.linalg.det(np.array(a.get_elements())))
    # print("distmat: ", a.det())

    # RANK
    # print("numpy: ", np.linalg.matrix_rank(np.array(a.get_elements())))
    # print("distmat: ", a.rank())

    # LINEAR SYSTEM SOLUTION
    print(a.lu_solve(b))


if __name__ == "__main__":
    main()

