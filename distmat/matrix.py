import random
import ray
import tasks as t

class Matrix:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = [[round(val, 8) for val in row] for row in data]

        else:
            raise ValueError("Input must be a list")

    def __str__(self):
        tmp = ''

        for row in self.data:
            for item in row:
                tmp = tmp + '{:12}\t'.format(item)

            tmp = tmp + '\n'
        return tmp

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def shape(self):
        num_rows = len(self.data)
        num_cols = len(self.data[0]) if num_rows > 0 else 0
        return (num_rows, num_cols)

    def get(self):
        return self.data

    @staticmethod
    def random_int(rows, cols, l, u):
        if rows > 1 and cols > 1:
            data = [[random.randint(l, u) for _ in range(rows)]
                    for _ in range(cols)]

        elif rows == 1 and cols > 1:
            data = [random.randint(l, u) for _ in range(cols)]

        elif rows > 1 and cols == 1:
            data = [[random.randint(l, u)]
                    for _ in range(cols) for _ in range(rows)]

        return Matrix(data)

    @staticmethod
    def random_float(rows, cols, l, u):
        if rows > 1 and cols > 1:
            data = [[random.uniform(l, u) for _ in range(rows)]
                    for _ in range(cols)]

        elif rows == 1 and cols > 1:
            data = [random.uniform(l, u) for _ in range(cols)]

        elif rows > 1 and cols == 1:
            data = [[random.uniform(l, u)]
                    for _ in range(cols) for _ in range(rows)]

        return Matrix(data)

    def is_matrix(self):
        rows, cols = self.shape()
        return rows > 1 and cols > 1

    def is_square(self):
        rows, cols = self.shape()
        return rows == cols

    def is_vector(self):
        rows, cols = self.shape()
        return rows == 1 ^ cols == 1

    def is_row_vector(self):
        rows, cols = self.shape()
        return rows == 1 and cols > 1

    def is_col_vector(self):
        rows, cols = self.shape()
        return cols == 1 and rows > 1

    def is_scalar(self):
        rows, cols = self.shape()
        return rows == cols and cols == 1

    @staticmethod
    def same_size(A, B):
        '''
        Return true if A and B have the same size
        '''
        a_rows, a_cols = A.shape()
        b_rows, b_cols = B.shape()

        if a_rows == b_rows and a_cols == b_cols:
            return True

        # Check if A and B are both column vectors or row vectors and have the same size
        if (a_rows == 1 and b_rows == 1) or (a_cols == 1 and b_cols == 1):
            return True

        return False

    def make_column_vector(self):
        if self.is_vector():
            if self.get_type() == 2:
                return self.transpose()

            else:
                return self

        else:
            raise ValueError("Input is not a valid vector")

    def make_row_vector(self):
        if self.is_vector():
            if self.get_type() == 3:
                return self.transpose()

            else:
                return self

        else:
            raise ValueError("Input is not a valid vector")

    def get_square_submatrices(self, order):
        '''
        Auxiliary function for the rank() function
        '''
        data = self.get()
        rows, cols = self.shape()
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(cols - order + 1):
                submatrix = []

                for row in range(order):
                    submatrix.append(
                        data[start_row + row][start_col:start_col + order])

                submatrices.append(Matrix(submatrix))

        return submatrices

    def transpose(self):
        data = self.get()
        transpose_array = None

        if self.is_row_vector():
            transpose_array = [[i] for i in data]

        elif self.is_col_vector():
            transpose_array = [i[0] for i in data]

        elif self.is_matrix():
            transpose_array = [[row[column] for row in data]
                               for column in range(len(data[0]))]

        return Matrix(transpose_array)

    def minor(self, i, j):
        '''
        Extract a minor matrix by removing the ith row and jth column
        '''

        data = self.get()
        minor_data = [row[:j] + row[j + 1:]
                      for row_idx, row in enumerate(data) if row_idx != i]

        return Matrix(minor_data)

    def det(self):
        if self.is_square():
            data = self.get()
            _, cols = self.shape()

            if cols == 1:
                return data[0][0]

            elif cols == 2:
                return (data[0][0] * data[1][1]) - (data[0][1] * data[1][0])

            else:
                det_value = 0

                for j in range(cols):
                    minor = self.minor(0, j)
                    det_value += ((-1) ** j) * data[0][j] * minor.det()

                return det_value

        else:
            raise ValueError(
                "Cannot compute determinant of a non-square matrix")

    def rank(self):
        rows, cols = self.shape()
        j1 = min(rows, cols)

        for i in range(j1, 1, -1):
            if self.get_square_submatrices(i) != -1:
                return i

    @staticmethod
    def dot(A, B):
        if A.is_matrix() and B.is_matrix():
            a_rows, a_cols = A.shape()
            b_rows, b_cols = B.shape()

            if a_cols == b_rows:
                result = [[0] * b_cols for _ in range(a_rows)] # create empty matrix
                futures = []

                for i in range(a_rows):
                    for j in range(b_cols):
                        for k in range(a_cols):
                            # result[i][j] += A.data[i][k] * B.data[k][j]
                            futures.append(((i, j), t.dot_calc.remote(A, B, i, j, k)))
                
                for future in futures:
                    i, j = future[0]
                    result[i][j] += ray.get(future[1])

                return Matrix(result)
            else:
                raise ValueError(
                    "Matrix dimensions do not match for dot product")
        else:
            raise ValueError("Dot product requires a Matrix object")

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif self.det() == 0:
            raise Exception("Matrix is not invertible")

        else:
            rows, cols = self.shape()
            data = self.get()

            det = self.det()

            # special case for 2x2 matrix:
            if rows == cols == 2:
                m = [[data[1][1] / det, -1 * data[0][1] / det],
                     [-1 * data[1][0] / det, data[0][0] / det]]

                return Matrix([[round(i, 8) for i in j] for j in m])

            # find matrix of cofactors
            cof_matrix = []

            for row in range(rows):
                cof_row = []

                for column in range(cols):
                    minor = self.minor(row, column)

                    cof_row.append(((-1)**(row + column)) * minor.det())

                cof_matrix.append(cof_row)

            cof_matrix = Matrix(cof_matrix).transpose()

            cof_rows, cof_cols = cof_matrix.shape()
            cof_data = cof_matrix.get()

            for row in range(cof_rows):
                for column in range(cof_cols):
                    cof_data[row][column] = cof_data[row][column] / det

            return Matrix([[round(i, 8) for i in j] for j in cof_matrix])
