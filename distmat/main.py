import ray
from matrix import Matrix
import time
import csv
    
def test_dot(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*runs
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_int(n, n, -10**8, 10**8)
            b = Matrix.random_float(n, n, -99, 99)

            t0 = time.time()
            Matrix.dot(a,b)
            t1 = time.time()

            sub_run.append(t1-t0)

            counter += 1
            print(f"run # {counter}/{max_n}: {t1-t0}")

        measures.append(sub_run)

    return measures

def test_det(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*runs
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_float(n, n, -10**8, 10**8)

            t0 = time.time()
            a.det()
            t1 = time.time()

            sub_run.append(t1-t0)

            counter += 1
            print(f"run # {counter}/{max_n}: {t1-t0}")

        measures.append(sub_run)

    return measures

def test_rank(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*runs
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_float(n, n, -10**8, 10**8)

            t0 = time.time()
            a.rank()
            t1 = time.time()

            sub_run.append(t1-t0)

            counter += 1
            print(f"run # {counter}/{max_n}: {t1-t0}")

        measures.append(sub_run)

    return measures

def test_inv(l, u, runs):
    '''Make tests for matrices size l...u'''
    max_n = (u-l)*runs
    counter = 0
    measures = []
    
    for n in range(l, u):
        sub_run = []
        sub_run.append(n) # matrix size

        for i in range(runs):
            a = Matrix.random_float(n, n, -10**8, 10**8)

            t0 = time.time()
            a.inv()
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

    test_results = test_inv(2, 8, 3)

    with open("test_results/test_inv_2_8_3.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerows(test_results)

    # a = Matrix.random_float(8, 8, -10**8, 10**8)
    # t0 = time.time()
    # a.inv()
    # print(time.time() - t0)
