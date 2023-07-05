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

    for op in operations():
        exec_time_single = op(a_base, b_base)
        exec_time_parallel = op(a_ray, b_ray)

        print('time single: ', exec_time_single)
        print('time parallel: ', exec_time_parallel)
    
def product(a, b):
    start = time()
    
    return time() - start()

def determinant(a):
    pass

def inverse(a):

    pass


operations = {
    "p": product,
    "d": determinant,
    "i": inverse
}
