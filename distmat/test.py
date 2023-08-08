
from matrix import Matrix
import numpy as np
import random

def main():
    A = Matrix([
        [4, 0, 2, 6],
        [8, 9, 1, 3],
        [5, 8, 4, 1],
        [6, 3, 0, 2]
    ])

    elements = [[random.randint(0, 99) for _ in range(8)] for _ in range(8)]
    B = Matrix(elements)

    print(np.linalg.det(np.array(elements)))
    
    print(B.det())

if __name__ == "__main__":
    main()

