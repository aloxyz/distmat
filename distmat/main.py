import ray
import logging
from matrix import Matrix
import numpy as np
import time
import csv

def test_dot_range(l, u, runs):
    measures = []
    sub_runs = []
    for n in range(l, u):
        for i in range(runs):
            a = Matrix.random_int(16, 16, -10**n, 10**n)
            b = Matrix.random_float(16, 16, -10**n, 10**n)

            t0 = time.time()
            Matrix.dot(a,b)
            t1 = time.time()

            sub_runs.append(t1-t0)
            print(t1-t0)

        measures.append(t1-t0)

    return measures
    
def test_dot_size(l, u, runs):
    measures = []
    sub_runs = []
    for n in range(l, u):
        for i in range(runs):
            a = Matrix.random_int(n, n, -99, 99)
            b = Matrix.random_float(n, n, -99, 99)

            t0 = time.time()
            Matrix.dot(a,b)
            t1 = time.time()

            sub_runs.append(t1-t0)
            print(t1-t0)

        measures.append(sub_runs)

    return measures


if __name__ == "__main__":
    if ray.is_initialized:
        ray.shutdown()
    ray.init(include_dashboard=True)

    test_results = test_dot_size(2, 8, 4)    

    with open("output.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(test_results)

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
    # print("\ndistmat:\n", a.inv())
    # print("numpy: \n", np.linalg.inv(np.array(a.get())))
    
