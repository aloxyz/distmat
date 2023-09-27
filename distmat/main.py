import ray
import logging
from matrix import Matrix
import numpy as np

if __name__ == "__main__":
    a = Matrix.random_int(8, 8, -99, 99)
    b = Matrix.random_float(8, 8, -99, 99)

    # DOT PRODUCT
    # print("\ndistmat:\n", Matrix.dot(a,b))
    # print("numpy: \n", np.dot(np.array(a.get()), np.array(b.get())))

    # DETERMINANT
    # print("\nnumpy: ", np.linalg.det(np.array(a.get())))
    # print("distmat: ", a.det())

    # RANK
    # print("\nnumpy: ", np.linalg.matrix_rank(np.array(a.get())))
    # print("distmat: ", a.rank())

    # INVERSE
    print("\ndistmat:\n", a.inv())
    print("numpy: \n", np.linalg.inv(np.array(a.get())))

    if ray.is_initialized:
        ray.shutdown()
    ray.init(include_dashboard=True)
    
