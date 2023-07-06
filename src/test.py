from mat.raymatrix import RayMatrix
from mat.matrix import Matrix

import ray
import random

def main():
    ray.init()
    A = RayMatrix([
        [1, 2, 3],
        [4, 5, 7],
        [5, 3, 2],
        [9, 5, 6],
        [1, 3, 8]])

    B = RayMatrix([[random.randint(0, 99) for _ in range(5)] for _ in range(5)])
    C = RayMatrix([[random.randint(0, 99) for _ in range(40)] for _ in range(40)])

    D = RayMatrix([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

    E = RayMatrix([
        [4, 10, 2, 6],
        [8, 9, 1, 3],
        [5, 8, 4, 1],
        [6, 3, 0, 2]
    ])
    F = Matrix([
        [4, 10, 2, 6],
        [8, 9, 1, 3],
        [5, 8, 4, 1],
        [6, 3, 0, 2]
    ])

    # print(E.inv())
    # print(F.inv())

    # print(RayMatrix.product(B,C))
    # print(E.det())

    print(B)
    print(len(B.get_square_submatrices(4)))
    [print(m) for m in B.get_square_submatrices(4)]
    B.get_square_submatrices(2)
    ray.shutdown()


if __name__ == "__main__":
    main()

