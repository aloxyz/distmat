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

    def minor(self, i, j):
        minor_elements = [row[:j] + row[j + 1:] for row_idx, row in enumerate(self.elements) if row_idx != i]
        return RayMatrix(minor_elements)

    def det(self):
        if self.is_square():
            size = self.size()["rows"]
            a = self.get()

            if size == 1:
                return a[0][0]

            elif size == 2:
                return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

            else:
                '''
                NON FUNZIONA
                sum = 0

                                for i in range(size):
                                    print(i)

                                    futures = self.task_det.remote(self=self, elements=a, i=0)
                                    print(ray.get(futures))

                                    sum += ray.get(futures)

                                return sum'''

                futures = self.task_det.remote(self=self, elements=a, i=0)
                return ray.get(futures)
        
        else:
            raise ValueError("Cannot compute determinant of a non-square matrix")

    def det2(self):
        if self.is_square():
            size = self.size()["rows"]
            a = self.get()

            if size == 1:
                return a[0][0]

            elif size == 2:
                return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

            else:
                sum = 0

                for i in range(1, size):
                    print(i)

                    futures = self.task_det.remote(self=self, elements=a, i=i)
                    print(ray.get(futures))

                    sum += ray.get(futures)

                return sum

        else:
            raise ValueError("Cannot compute determinant of a non-square matrix")

    @ray.remote
    def task_det2(self, elements, i):
        size = len(elements)
        submatrix_det_sum = 0
        mats = self.get_square_submatrices(i)

        for j in range(1, size):
            submatrix_det = mats[j].det2()
            submatrix_det_sum += elements[i][j] * ((-1) ** (i + j + 2)) * submatrix_det

        return submatrix_det_sum
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
    
    @ray.remote
    def task_inv_cof(self, a, i, j):
        det = self.minor(i, j).det()
        return (i, j, a[i][j] * ((-1) ** (i + j + 2)) * det)

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif self.det() == 0:
            raise Exception("Matrix is not invertible")

        else:
            size = self.size()["rows"]
            a = self.get()
            cof_arr = [[0] * size for _ in range(size)]

            tasks = []
            for i in range(size):
                for j in range(size):
                    tasks.append(self.task_inv_cof.remote(self=self, a=a, i=i, j=j))

            results = ray.get(tasks)
            for i, j, value in results:
                cof_arr[i][j] = value

            cof_matrix = Matrix(cof_arr)
            return cof_matrix.scalar_product(1 / self.det())

    @staticmethod
    @ray.remote
    def task_multiply(a, b, i, j, k):
        return a[i][k] * b[k][j]

    @staticmethod
    @ray.remote
    def task_sum(results):
        return sum(results)

    @staticmethod
    def product(a, b):
        a_columns = a.size()["columns"]
        a_rows = a.size()["rows"]

        b_columns = b.size()["columns"]
        b_rows = b.size()["rows"]

        if a_rows != b_columns:
            raise ValueError("Number of columns of the first matrix must match the number of rows of the second matrix")

        else:
            a_elements = a.get()
            b_elements = b.get()

            result = [[0] * b_columns for _ in range(a_rows)]
            tasks = []

            for i in range(a_rows):
                for j in range(b_columns):
                    elements_to_multiply = []
                    
                    for k in range(a_columns):
                        elements_to_multiply.append(
                            RayMatrix.task_multiply.remote(a=a_elements, b=b_elements, i=i, j=j, k=k)
                        )
                    
                    tasks.append(RayMatrix.task_sum.remote(results=ray.get(elements_to_multiply)))

            results = ray.get(tasks)

            for i in range(a_rows):
                for j in range(b_columns):
                    result[i][j] = results.pop(0)

            return RayMatrix(result)
