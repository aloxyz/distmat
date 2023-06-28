from mat.matrix import Matrix

import ray


class RayMatrix(Matrix):
    def __init__(self, elements):
        super().__init__(elements)

    @ray.remote
    def mod_rank_det(submatrix, j):
        if submatrix.det() != 0:
            return j

    def rank(self):
        rows = self.size()["rows"]
        columns = self.size()["columns"]

        j1 = min(rows, columns)

        for j in range(j1, 1, -1):            
            jth_submatrices = self.get_square_submatrices(j)
            
            for submatrix in jth_submatrices:
                return self.mod_rank_det.remote(submatrix, j)

