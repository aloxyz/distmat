import random


class Matrix:
    def __init__(self, elements):
        if Matrix.is_array_scalar(elements):
            self.type = 1
            self.rows = 1
            self.columns = 1

        elif Matrix.is_array_row(elements):
            self.type = 2
            self.rows = len(elements)
            self.columns = 1

        elif Matrix.is_array_column(elements):
            self.type = 3
            self.rows = 1
            self.columns = len(elements)

        elif Matrix.is_array_2d(elements):
            # Check for same-length rows
            for i in elements:
                if len(i) != len(elements[0]):
                    raise ValueError("Invalid row size")

            self.rows = len(elements[0])
            self.columns = len(elements)

            self.type = 4

        else:
            raise ValueError("Cannot determine array type")

        self.elements = elements

    # def __str__(self):
    #     elements = self.get_elements()

    #     tmp = ''

    #     if self.is_array_column(elements):
    #         tmp = [[i] for i in elements]

    #     elif self.is_array_row(elements):
    #         tmp = elements

    #     else:
    #         tmp = "\n"
    #         for column in elements:
    #             tmp += [i for i in column].join('\t') + '\n'

    #     return tmp

    # def print(self):
    #     elements = self.get_elements()

    #     print(elements())

    def __str__(self):
        if self.get_type() <= 2:
            return ' ' + ' '.join(['{:2}'.format(i) for i in self.get_elements()]) + '\n\n'

        if self.get_type() >= 3:
            return '\n' + '\n'.join([''.join(['{:8}'.format(item) for item in row]) for row in self.get_elements()]) + '\n\n'

    @staticmethod
    def random(rows, columns, l, u):
        if rows > 1 and columns > 1:
            elements = [[random.randint(l, u) for _ in range(rows)]
                        for _ in range(columns)]

        elif rows == 1 and columns > 1:
            elements = [random.randint(l, u) for _ in range(columns)]

        elif rows > 1 and columns == 1:
            elements = [[random.randint(l, u)]
                        for _ in range(columns) for _ in range(rows)]

        return Matrix(elements)

    def get_elements(self):
        '''
        Returns a 2D array of the matrix elements 
        '''

        return self.elements

    def get_size(self):
        '''
        Returns the tuple (numberof_rows, numberof_columns)
        '''

        return (self.rows, self.columns)

    def get_type(self):
        '''
        Returns:
            int: An integer code representing the type of the matrix or vector.
                - 1: Scalar (1x1 matrix)
                - 2: Row Vector (1 row, multiple columns)
                - 3: Column Vector (1 column, multiple rows)
                - 4: Matrix (multiple rows and columns)
        '''
        return self.type

    def is_square(self):
        rows, columns = self.get_size()

        return rows == columns

    @staticmethod
    def is_array_scalar(array):
        return isinstance(array, (int, float))

    @staticmethod
    def is_array_row(array):
        return isinstance(array, list) and len(array) >= 1 and isinstance(array[0], (int, float))

    @staticmethod
    def is_array_column(array):
        return isinstance(array, list) and len(array) >= 1 and isinstance(array[0], list) and len(array[0]) == 1

    @staticmethod
    def is_array_2d(array):
        return not (Matrix.is_array_row(array) and Matrix.is_array_column(array))

    def is_vector(self):
        return self.get_type() == 2 or self.get_type() == 3

    @staticmethod
    def product(A, B):
        a_rows, a_columns = A.get_size()
        _, b_columns = B.get_size()

        if a_rows != b_columns:
            raise ValueError(
                "Number of columns of first matrix must match the number of rows of second matrix")

        else:
            a_elements = A.get_elements()
            b_elements = B.get_elements()

            result = [[[0] * i for i in range(b_columns)]
                      for j in range(a_rows)]

            for i in range(a_rows):
                for j in range(b_columns):
                    result[i][j] = 0

                    for k in range(a_columns):
                        result[i][j] += a_elements[i][k] * b_elements[k][j]

        return Matrix(result)

    def transpose(self):
        elements = self.get_elements()
        rows, columns = self.get_size()
        transpose_array = None

        if self.get_type() == 2:
            transpose_array = [[i] for i in elements]

        elif self.get_type() == 3:
            transpose_array = [i[0] for i in elements]

        elif self.get_type() == 4:
            transpose_array = [[row[column] for row in elements]
                               for column in range(len(elements[0]))]

        return Matrix(transpose_array)

    def minor(self, i, j):
        '''
        Extract a minor matrix by removing the ith row and jth column
        '''

        elements = self.get_elements()
        minor_elements = [row[:j] + row[j + 1:]
                          for row_idx, row in enumerate(elements) if row_idx != i]

        return Matrix(minor_elements)

    @staticmethod
    def same_size(A, B):
        '''
        Return true if A and B have the same size
        '''
        a_rows, a_columns = A.get_size()
        b_rows, b_columns = B.get_size()

        if a_rows == b_rows and a_columns == b_columns:
            return True

        # Check if A and B are both column vectors or row vectors and have the same size
        if (a_rows == 1 and b_rows == 1) or (a_columns == 1 and b_columns == 1):
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

    @staticmethod
    def dot(A, B):
        if not A.is_vector() and isinstance(B, (int, float, complex)):      # matrix * scalar
            a_elements = A.get_elements()
            result_array = [[a * B for a in column] for column in a_elements]

            return Matrix(result_array)

        if A.is_vector() and B.is_vector():     # vector * vector
            A = A.make_row_vector()
            B = B.make_row_vector()

            if Matrix.same_size(A, B):
                a_elements = A.get_elements()
                b_elements = B.get_elements()

                result = 0

                for a, b in zip(a_elements, b_elements):
                    result += a * b

                return result

            else:
                raise ValueError("Vectors must be of the same size")

        if A.is_vector() and not B.is_vector():    # vector * matrix
            result_array = []

            # if row vector
            if A.get_type() == 2:
                b_elements = B.transpose().get_elements()
        
                for column in b_elements:
                    sum = 0

                    for a, b in zip(a_elements, column):
                        sum += a * b

                    result_array.append(sum)

            # if column vector
            elif A.get_type() == 3:
                for row in A.get_elements():
                    row_sum = 0

                    for a, b in zip(row, B.get_elements()):
                        row_sum += a * b[0]

                    result_array.append([row_sum])

            return Matrix(result_array)

        if not A.is_vector() and B.is_vector():    # matrix * vector
            result_array = []

            # if row vector
            if B.get_type() == 2:
                for row in A.get_elements():
                    row_sum = 0

                    for a, b in zip(row, B.get_elements()):
                        row_sum += a * b

                    result_array.append(row_sum)
            
            # if column vector
            elif B.get_type() == 3:
                for row in A.get_elements():
                    row_sum = 0

                    for a, b in zip(row, B.get_elements()):
                        row_sum += a * b[0]

                    result_array.append([row_sum])

            return Matrix(result_array)

        # TODO
        if not A.is_vector() and not B.is_vector():     # matrix * matrix
            a_rows, a_columns = A.get_size()
            b_rows, b_columns = B.get_size()

            if a_columns == b_rows:
                result_array = Matrix.empty_2d_array(a_rows, b_columns)

                return Matrix(result_array)

            else:
                raise ValueError(
                    "Matrix dimensions must be compatible for matrix multiplication")

    @staticmethod
    def empty_2d_array(rows, columns):
        return [[0] * rows for _ in range(columns)]

    @staticmethod
    def empty_row_array(n):
        return [0 for _ in range(n)]

    @staticmethod
    def empty_column_array(n):
        return [[0] for _ in range(n)]

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif self.det() == 0:
            raise Exception("Matrix is not invertible")

        else:
            rows, _ = self.get_size()

            cof_elements = [[0] * rows for _ in range(rows)]

            for i in range(rows):
                for j in range(rows):
                    cof_elements[i][j] = (
                        (-1) ** (i + j + 2)) * self.minor(i, j).det()

            cof_matrix = Matrix(cof_elements)
            det_reciprocal = 1 / self.det()
            inv_matrix = Matrix.dot(cof_matrix, det_reciprocal)

            return inv_matrix

    def det(self):
        if self.is_square():
            elements = self.get_elements()
            _, columns = self.get_size()

            if columns == 1:
                return elements[0][0]

            elif columns == 2:
                return (elements[0][0] * elements[1][1]) - (elements[0][1] * elements[1][0])

            else:
                det_value = 0

                for j in range(columns):
                    minor = self.minor(0, j)
                    det_value += ((-1) ** j) * elements[0][j] * minor.det()

                return det_value

        else:
            raise ValueError(
                "Cannot compute determinant of a non-square matrix")

    def get_square_submatrices(self, order):
        '''
        Auxiliary function for the rank() function
        '''
        elements = self.get_elements()
        rows, columns = self.get_size()
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(columns - order + 1):
                submatrix = []

                for row in range(order):
                    submatrix.append(
                        elements[start_row + row][start_col:start_col + order])

                submatrices.append(Matrix(submatrix))

        return submatrices

    def rank(self):
        rows, columns = self.get_size()
        j1 = min(rows, columns)

        for i in range(j1, 1, -1):
            if self.get_square_submatrices(i) != -1:
                return i
