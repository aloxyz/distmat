
from matrix import Matrix

import random

def main():
    A = Matrix([
        [4, 0, 2, 6],
        [8, 9, 1, 3],
        [5, 8, 4, 1],
        [6, 3, 0, 2]
    ])

    B = Matrix([[random.randint(0, 99) for _ in range(4)] for _ in range(4)])

    print(A, B)
    print(Matrix.product(A,B))

if __name__ == "__main__":
    main()

