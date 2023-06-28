from mat.matrix import Matrix
import ray

class RayMatrix(Matrix):
    def __init__(self, elements):
        super().__init__(elements)

    @ray.remote
    def task_rank_det(submatrix, j):
        if submatrix.det() != 0:
            return j
    
    @ray.remote
    def task_get_square_submatrix(self, start_row, start_col, row, order):
        return self.elements[start_row + row][start_col:start_col + order]

    @ray.remote
    def task_det(self, elements, i):
        size = len(elements)
        submatrix_det_sum = 0

        for j in range(size):
            submatrix_det = self.minor(i=i, j=j).det()
            submatrix_det_sum += elements[i][j] * ((-1) ** (i + j + 2)) * submatrix_det

        return submatrix_det_sum

    def get_square_submatrices(self, order):
        rows = self.size()["rows"]
        cols = self.size()["columns"]
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(cols - order + 1):
                submatrix = []
                
                for row in range(order):
                    futures = self.task_get_square_submatrix.remote(self=self, start_row=start_row, start_col=start_col, row=row, order=order)
                    
                    submatrix.append(ray.get(futures))
                
                submatrices.append(RayMatrix(submatrix))

        return submatrices

    def det(self):
        if self.is_square():
            size = self.size()["rows"]
            a = self.get()

            if size == 1:
                return a[0][0]

            elif size == 2:
                return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

            else:
                sum = 0

                for i in range(size):
                    futures = self.task_det.remote(self=self, elements = a, i=i)

                    sum += ray.get(futures)

                return sum

    def rank(self):
        rows = self.size()["rows"]
        columns = self.size()["columns"]

        j1 = min(rows, columns)

        for j in range(j1, 1, -1):            
            jth_submatrices = self.get_square_submatrices(j)
            

            tasks = []

            for submatrix in jth_submatrices:
                tasks.append(self.task_rank_det.remote(submatrix, j))


            ready_tasks, _ = ray.wait(tasks, num_returns = max(rows, columns) - j + 1)
            for ready_task in ready_tasks:
                    result = ray.get(ready_task)

                    if result is not None:
                        return result
                    
        return 0