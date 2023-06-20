from mat import matrix as mat

def main():
    A = mat.Matrix([
        [1, 0, 2, 5],
        [0, 3, -1, 6],
        [3, 2, 4, 8],
        [1, 2, 6, 9],
        [3, 4, 6, 8]
    ])

    B = mat.Matrix([
        [4, 1],
        [-2, 2],
        [0, 3]
    ])

    print(A.range())


if __name__ == "__main__":
    main()

