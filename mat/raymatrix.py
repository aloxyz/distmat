from mat.matrix import Matrix
import ray

class RayMatrix(Matrix):
    def __init__(self, elements):
        super().__init__(elements)

    @ray.remote
    def task_rank_det(submatrix, j):
        if submatrix.det() != 0:
            return j

    def rank(self):
        rows = self.size()["rows"]
        columns = self.size()["columns"]

        j1 = min(rows, columns)

        for j in range(j1, 1, -1):            
            jth_submatrices = self.get_square_submatrices(j)
            

            tasks = []

            for submatrix in jth_submatrices:
                tasks.append(self.task_rank_det.remote(submatrix, j))


            ready_tasks, _ = ray.wait(tasks, num_returns=2) # num_returns must be calculated
            for ready_task in ready_tasks:
                    result = ray.get(ready_task)

                    if result is not None:
                        return result
                    
        return 0