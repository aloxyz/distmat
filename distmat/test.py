
from matrix import Matrix
import numpy as np

def main():

    a = Matrix.random(3, 1, -99, 99)
    b = Matrix.random(3, 3, -99, 99)

    print(f"{a}*{b}= {Matrix.dot(a,b)}")

    print(np.dot(np.array(a.get_elements()), np.array(b.get_elements())))
    # print("numpy: ", np.linalg.inv(np.array(elements)))
    # print("distmat: ", Matrix.inv(A))


if __name__ == "__main__":
    main()

