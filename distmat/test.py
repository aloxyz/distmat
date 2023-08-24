
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random(1, 3, -99, 99)
    print(a)

    b = Matrix.random(2, 3, -99, 99)
    print(b)

    print(Matrix.dot(a,b))

    print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))
    # print("numpy: ", np.linalg.inv(np.array(elements)))
    # print("distmat: ", Matrix.inv(A))


if __name__ == "__main__":
    main()

