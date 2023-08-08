from mat.matrix import Matrix
import ray


class RayMatrix(Matrix):
    def __init__(self, elements):
        super().__init__(elements)

    @ray.remote
    def task_rank_det(submatrix, j):
        if submatrix.det() != 0:
            return j

    @staticmethod
    @ray.remote
    def task_scalar_product(row, scalar):
        for j in range(len(row)):
            row[j] *= scalar

        return row

    # @ray.remote
    # def task_gen_submatrix(elements, start_row, start_col, order):
    #     futures = []

    #     for row in range(order):
    #         futures.append(elements[start_row + row][start_col:start_col + order])

    #     return futures

    # def get_square_submatrices(self, order):
    #     elements_id = ray.put(self.get())

    #     rows = self.size()["rows"]
    #     cols = self.size()["columns"]
    #     futures = []

    #     for start_row in range(rows - order + 1):
    #         for start_col in range(cols - order + 1):
    #             futures.append(self.task_gen_submatrix.remote(elements=elements_id, start_row=start_row, start_col=start_col, order=order))

    #     return [RayMatrix(m) for m in ray.get(futures)]


    def minor(self, i, j):
        minor_elements = [row[:j] + row[j + 1:] for row_idx, row in enumerate(self.elements) if row_idx != i]
        return RayMatrix(minor_elements)

    @staticmethod
    @ray.remote
    def task_det(submatrix):
        return submatrix.det()

    def det(self):
        if self.is_square():
            cols = self.size()["columns"]
            elements = self.get()

            if cols == 1:
                return elements[0][0]

            elif cols == 2:
                return (elements[0][0] * elements[1][1]) - (elements[0][1] * elements[1][0])

            else:
                # Iterative computation of determinant
                submatrices = [[self.minor(row, col) for col in range(cols)] for row in range(cols)]
                determinants = []
                batch_size = 10  # Adjust batch size as needed

                for i in range(0, cols, batch_size):
                    batch_results = ray.get([self.task_det.remote(submatrix) for submatrix_row in submatrices[i:i+batch_size] for submatrix in submatrix_row])
                    determinants.extend(batch_results)

                determinant = 0

                for col in range(cols):
                    sign = (-1) ** col
                    sub_determinants = [determinants[row * cols + col] for row in range(cols)]
                    determinant += sign * elements[0][col] * self._cofactor(sub_determinants)

                return determinant

        else:
            raise ValueError("Cannot compute determinant of a non-square matrix")

    @staticmethod
    def _cofactor(sub_determinants):
        n = len(sub_determinants)
        if n == 2:
            return sub_determinants[0] * sub_determinants[3] - sub_determinants[1] * sub_determinants[2]
        else:
            return sum(
                (-1) ** i * sub_determinants[i] * RayMatrix._cofactor(sub_determinants[:i] + sub_determinants[i + 1:])
                for i in range(n)
            )

    def rank(self):
        rows = self.size()["rows"]
        columns = self.size()["columns"]

        j1 = min(rows, columns)
        for j in range(j1, 1, -1):
            jth_submatrices = self.get_square_submatrices(j)
            tasks = []

            for submatrix in jth_submatrices:
                tasks.append(self.task_rank_det.remote(submatrix, j))

            ready_tasks, _ = ray.wait(tasks, num_returns=max(rows, columns) - j + 1)
            
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

            cof_matrix = RayMatrix(cof_arr)
            return cof_matrix.scalar_product(1 / self.det())

    @staticmethod
    @ray.remote
    def task_multiply(a, b, i, j, k):
        return a[i][k] * b[k][j]

    @staticmethod
    @ray.remote
    def task_sum(results):
        return sum(results)

    def product(self, b):
        a_columns = self.size()["columns"]
        a_rows = self.size()["rows"]

        b_columns = b.size()["columns"]

        if a_rows != b_columns:
            raise ValueError("Number of columns of the first matrix must match the number of rows of the second matrix")

        else:
            a_elements = self.get()
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

    def scalar_product(self, scalar):
        elems = self.get()
        res = []

        futures = []

        for r in elems:
            futures.append(RayMatrix.task_scalar_product.remote(r, scalar))

        res = ray.get(futures)

        return Matrix(res)
