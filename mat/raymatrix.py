from mat import matrix as mat
from mat import base_ops as bm

import ray


@ray.remote
class RayMatrix(mat.Matrix):

    def rank(self):
        j1 = min(self.size()['rows'], self.size()['columns'])

        for i in range(j1, 1, -1):
            if bm.get_submatrices_rank(self, i) != -1:
                return i
    pass
