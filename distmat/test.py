
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random(3, 3, -99, 99)
    b = Matrix.random(3, 3, -99, 99)

    # DOT PRODUCT
    # print(f"{a}*{b}= {Matrix.dot(a,b)}")
    # print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))
    # print(a, Matrix.dot(a, 2))

    # INVERSE
    print("numpy: \n", np.linalg.inv(np.array(a.get_elements())))
    print("\ndistmat: ", a.inv())

    # DETERMINANT
    # print("numpy: ", np.linalg.det(np.array(a.get_elements())))
    # print("distmat: ", a.det())

if __name__ == "__main__":
    main()

