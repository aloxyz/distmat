import ray
from matrix import Matrix
import time
import csv
    
def test_dot_size(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*5
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_int(n, n, -10**16, 10**16)
            b = Matrix.random_float(n, n, -99, 99)

            t0 = time.time()
            Matrix.dot(a,b)
            t1 = time.time()

            sub_run.append(t1-t0)

            counter += 1
            print(f"run # {counter}/{max_n}: {t1-t0}")

        measures.append(sub_run)

    return measures

def test_det_size(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*5
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_int(n, n, -10**16, 10**16)
            b = Matrix.random_float(n, n, -99, 99)

            t0 = time.time()
            Matrix.dot(a,b)
            t1 = time.time()

            sub_run.append(t1-t0)

            counter += 1
            print(f"run # {counter}/{max_n}: {t1-t0}")

        measures.append(sub_run)

    return measures



if __name__ == "__main__":
    if ray.is_initialized:
        ray.shutdown()
    ray.init(include_dashboard=True)

    # test_results = test_dot_size(2, 30, 5)
    test_results = test_dot_size(2, 30, 5)

    with open("test_results/test_dot_size_2_30_5.csv", "w") as f:
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
    
