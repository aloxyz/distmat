import random
import array as Array

class Matrix:
    def __init__(self, data):
        if isinstance(data, list):
            self.data = data

        else:
            raise ValueError("Input must be a list")

    def __str__(self):
        return str(self.data)

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
    def random_int(rows, columns, l, u):
        if rows > 1 and columns > 1:
            data = [[random.randint(l, u) for _ in range(rows)]
                        for _ in range(columns)]

        elif rows == 1 and columns > 1:
            data = [random.randint(l, u) for _ in range(columns)]

        elif rows > 1 and columns == 1:
            data = [[random.randint(l, u)]
                        for _ in range(columns) for _ in range(rows)]

        return Matrix(data)

    @staticmethod
    def random_float(rows, columns, l, u):
        if rows > 1 and columns > 1:
            data = [[random.uniform(l, u) for _ in range(rows)]
                        for _ in range(columns)]

        elif rows == 1 and columns > 1:
            data = [random.uniform(l, u) for _ in range(columns)]

        elif rows > 1 and columns == 1:
            data = [[random.uniform(l, u)]
                        for _ in range(columns) for _ in range(rows)]

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
    
    def mean(self):
        return sum(self.data) / len(self.data)

    def sum(self):
        return sum(self.data)

    def max(self):
        return max(self.data)

    def min(self):
        return min(self.data)

    def transpose(self):
        data = self.get()
        rows, columns = self.shape()
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

    def __add__(self, other):
        if isinstance(other, Matrix):
            self.make_row_vector()
            other.make_row_vector()

            a_data = self.get()
            b_data = other.get()

            if Matrix.same_size(self, other):
                result_array = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(a_data, b_data)]
                return Matrix(result_array)
            else:
                raise ValueError("Input matrices must be of the same size")

        else:
            raise ValueError("Addition can only be performed with another Matrix")
    
    def __sub__(self, other):
        if isinstance(other, Matrix):
            self.make_row_vector()
            other.make_row_vector()

            a_data = self.get()
            b_data = other.get()

            if Matrix.same_size(self, other):
                result_array = [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(a_data, b_data)]
                return Matrix(result_array)
            else:
                raise ValueError("Input matrices must be of the same size")

        else:
            raise ValueError("Subtraction can only be performed with another Matrix")

    def det(self):
        if self.is_square():
            data = self.get()
            _, columns = self.shape()

            if columns == 1:
                return data[0][0]

            elif columns == 2:
                return (data[0][0] * data[1][1]) - (data[0][1] * data[1][0])

            else:
                det_value = 0

                for j in range(columns):
                    minor = self.minor(0, j)
                    det_value += ((-1) ** j) * data[0][j] * minor.det()

                return det_value

        else:
            raise ValueError(
                "Cannot compute determinant of a non-square matrix")

    def get_square_submatrices(self, order):
        '''
        Auxiliary function for the rank() function
        '''
        data = self.get()
        rows, columns = self.shape()
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(columns - order + 1):
                submatrix = []

                for row in range(order):
                    submatrix.append(
                        data[start_row + row][start_col:start_col + order])

                submatrices.append(Matrix(submatrix))

        return submatrices
    
    def rank(self):
        rows, columns = self.shape()
        j1 = min(rows, columns)

        for i in range(j1, 1, -1):
            if self.get_square_submatrices(i) != -1:
                return i

    @staticmethod
    def dot(A, B):
        pass

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif self.det() == 0:
            raise Exception("Matrix is not invertible")

        else:
            rows, columns = self.shape()
            data = self.get()

            det = self.det()

            # special case for 2x2 matrix:
            if rows == columns == 2:
                return [[data[1][1] / det, -1 * data[0][1] / det],
                        [-1 * data[1][0] / det, data[0][0] / det]]

            # find matrix of cofactors
            cof_matrix = []

            for row in range(rows):
                cof_row = []

                for column in range(columns):
                    minor = self.minor(row, column)

                    cof_row.append(((-1)**(row + column)) * minor.det())

                cof_matrix.append(cof_row)

            cof_matrix = Matrix(cof_matrix).transpose()

            cof_rows, cof_columns = cof_matrix.shape()
            cof_data = cof_matrix.get()

            for row in range(cof_rows):
                for column in range(cof_columns):
                    cof_data[row][column] = cof_data[row][column] / det

            return cof_matrix
