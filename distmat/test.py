
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random_int(10, 10, -99, 99)
    b = Matrix.random_float(10, 10, -99, 99)

    print(a, b)

    # DOT PRODUCT
    # print(f"{a}*\n{b}=\n{Matrix.dot(a,b)}")
    # print(a, Matrix.dot(a, 2))
    # print(Matrix.dot(a, b))
    # print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))

    # OUTER PRODUCT
    print(f"{a}*\n{b}=\n{Matrix.outer_product(a,b)}")
    print(np.outer(np.array(a.get_elements()), np.array(b.get_elements())))

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
    print()

if __name__ == "__main__":
    main()

