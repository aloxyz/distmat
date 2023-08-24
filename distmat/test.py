
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random_int(3, 4, -99, 99)
    b = Matrix.random_float(4, 3, -99, 99)

    # DOT PRODUCT
    # print(f"{a}*{b}= {Matrix.dot(a,b)}")
    print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))
    # print(a, Matrix.dot(a, 2))
    print(Matrix.dot(a, b))

    # INVERSE
    # print("\ndistmat: ", a.inv())
    # print("numpy: \n", np.linalg.inv(np.array(a.get_elements())))

    # DETERMINANT
    # print("numpy: ", np.linalg.det(np.array(a.get_elements())))
    # print("distmat: ", a.det())

if __name__ == "__main__":
    main()

