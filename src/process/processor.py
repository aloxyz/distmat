import random
from process.generator import generate_matrix
import utils.config as cfg
from mat.matrix import Matrix
from mat.raymatrix import RayMatrix
from time import time


def exec_test(size):
    a = generate_matrix(size, size)
    b = generate_matrix(size, size)
    
    a_base = Matrix(a)
    a_ray = RayMatrix(a)

    b_base = Matrix(b)
    b_ray = RayMatrix(b)

    single_out = {}
    parallel_out = {}

    for func, call in operations.items():
        exec_time_single = call((a_base, b_base))
        exec_time_parallel = call((a_ray, b_ray))

        single_out[func] = exec_time_single
        parallel_out[func] = exec_time_parallel

        print('time single - ', func, ':', exec_time_single)
        print('time parallel - ', func, ':', exec_time_parallel)

    return single_out, parallel_out


def product(args):
    start = time()

    a = args[0]
    b = args[1]

    print(a.product(b))

    return time() - start


def determinant(args):
    start = time()

    a = args[0]

    print(a.det())
    return time() - start


def inverse(args):
    start = time()

    a = args[0]

    print(a.inv())
    return time() - start


def rank(args):
    start = time()

    a = args[0]

    print(a.rank())
    return time() - start


def scalar_product(args):
    start = time()

    a = args[0]
    scalar = random.randint(1, 8)

    print(a.scalar_product(scalar))
    return time() - start


operations = {
    "p": product,
    "d": determinant,
    "i": inverse,
    "sp": scalar_product,
    "r": rank
}
