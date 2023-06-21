from mat import matrix as mat

import ray


@ray.remote
class ParallelMatrix(mat.Matrix):
    pass
