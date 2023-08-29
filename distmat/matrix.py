import random


class Matrix:
    def __init__(self, elements):
        sanitized_elements = self.sanitize_elements(elements)
        
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
            return ' ' + ' '.join(['{:12.4f}'.format(i) for i in self.get_elements()]) + '\n\n'

        if self.get_type() >= 3:
            return '\n' + '\n'.join([''.join(['{:12.4f}'.format(item) for item in row]) for row in self.get_elements()]) + '\n\n'

    @staticmethod
    def sanitize_elements(elements):
        if isinstance(elements, list) and len(elements) == 1 and isinstance(elements[0], list):
            return elements[0]
        else:
            return elements


    @staticmethod
    def random_int(rows, columns, l, u):
        if rows > 1 and columns > 1:
            elements = [[random.randint(l, u) for _ in range(rows)]
                        for _ in range(columns)]

        elif rows == 1 and columns > 1:
            elements = [random.randint(l, u) for _ in range(columns)]

        elif rows > 1 and columns == 1:
            elements = [[random.randint(l, u)]
                        for _ in range(columns) for _ in range(rows)]

        return Matrix(elements)

    @staticmethod
    def random_float(rows, columns, l, u):
        if rows > 1 and columns > 1:
            elements = [[random.uniform(l, u) for _ in range(rows)]
                        for _ in range(columns)]

        elif rows == 1 and columns > 1:
            elements = [random.uniform(l, u) for _ in range(columns)]

        elif rows > 1 and columns == 1:
            elements = [[random.uniform(l, u)]
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
    def outer_product(A, B):
        print(A.get_elements())
        if A.is_vector() and B.is_vector():
            A = A.make_column_vector()
            B = B.make_row_vector()

            a_elements = A.get_elements()
            b_elements = B.get_elements()

            result_array = [[a[0] * b for b in b_elements] for a in a_elements]

            return Matrix(result_array)
        else:
            raise ValueError("Both inputs should be vectors")

    @staticmethod
    def dot(A, B):
        result_array = []

        if A.is_vector() and isinstance(B, (int, float, complex)):      # vector * scalar
            a_elements = A.get_elements()
            result_array = [a * B for a in a_elements]

            return Matrix(result_array)

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

            if a_rows != b_columns:
                raise ValueError(
                    "Number of columns of first matrix must match the number of rows of second matrix")

            else:
                a_elements = A.get_elements()
                b_elements = B.get_elements()

                result_array = Matrix.empty_2d_array(a_rows, b_columns)

                for i in range(a_rows):
                    for j in range(b_columns):
                        for k in range(a_columns - 1):
                            result_array[i][j] += a_elements[i][k] * \
                                b_elements[k][j]

            return Matrix(result_array)

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
            rows, columns = self.get_size()
            elements = self.get_elements()

            det = self.det()

            # special case for 2x2 matrix:
            if rows == columns == 2:
                return [[elements[1][1] / det, -1 * elements[0][1] / det],
                        [-1 * elements[1][0] / det, elements[0][0] / det]]

            # find matrix of cofactors
            cof_matrix = []

            for row in range(rows):
                cof_row = []

                for column in range(columns):
                    minor = self.minor(row, column)

                    cof_row.append(((-1)**(row + column)) * minor.det())

                cof_matrix.append(cof_row)

            cof_matrix = Matrix(cof_matrix).transpose()

            cof_rows, cof_columns = cof_matrix.get_size()
            cof_elements = cof_matrix.get_elements()

            for row in range(cof_rows):
                for column in range(cof_columns):
                    cof_elements[row][column] = cof_elements[row][column] / det

            return cof_matrix
    
    @staticmethod
    def add(A, B):
        a_elements = A.get_elements()
        b_elements = B.get_elements()

        if Matrix.same_size(A, B):
            result_array = [[a + b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(a_elements, b_elements)]

            return Matrix(result_array)
        
        else:
            raise ValueError("Input matrices must be of same size")

    def sub(A, B):
        a_elements = A.get_elements()
        b_elements = B.get_elements()

        # if Matrix.same_size(A, B):
        result_array = [[a - b for a, b in zip(row_a, row_b)] for row_a, row_b in zip(a_elements, b_elements)]
        
        return Matrix(result_array)
    
        # else:
        #     raise ValueError("Input matrices must be of same size")


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

    def lu_solve(self, b):
        """x = lu_solve(L, U, b) is the solution to L U x = b
       L must be a lower-triangular matrix
       U must be an upper-triangular matrix of the same size as L
       b must be a vector of the same leading dimension as L
        
        https://courses.physics.illinois.edu/cs357/sp2020/notes/ref-9-linsys.html
        """

        L, U = self.lu_decomp()

        y = Matrix.fwd_sub(L, b)
        x = Matrix.back_sub(U, y)
        
        return x

    def lu_decomp(self):
        n, _ = self.get_size()

        if n == 1:
            L = Matrix([[1]])
            U = self.copy()
            return (L, U)

        elements = self.get_elements()

        A11 = elements[0][0]
        A12 = elements[0][1:]
        A21 = [row[0] for row in elements[1:]]
        A22 = [row[1:] for row in elements[1:]]

        L11 = 1
        U11 = A11
        L12 = Matrix.empty_row_array(n-1)
        U12 = A12.copy()

        L21 = Matrix.dot(Matrix([A21]), 1/U11)  # Matrix(A21.copy()) / U11
        U21 = Matrix.empty_row_array(n-1)

        S22 = Matrix.sub(Matrix(A22), Matrix.outer_product(L21, Matrix(U12)))
        (L22, U22) = S22.lu_decomp()

        L = Matrix([[L11] + L12.get_elements()] + [L21.get_elements(), L22.get_elements()])
        U = Matrix([[U11] + U12.get_elements()] + [U21.get_elements(), U22.get_elements()])

        return (L, U)

    @staticmethod
    def fwd_sub(L, b):
        """x = forward_sub(L, b) is the solution to L x = b
        L must be a lower-triangular matrix
        b must be a vector of the same leading dimension as L
        """
        n, _ = L.get_size()
        x = Matrix.empty_row_array(n)

        L_elements = L.get_elements()
        b_elements = b.get_elements()

        for i in range(n):
            sum = b_elements[i]

            for j in range(i-1):
                sum -=  L_elements[i][j] * x[j]
            
            x[i] = sum / L_elements[i][i]

        return Matrix(x)
    
    @staticmethod
    def back_sub(U, b):
        """x = back_sub(U, b) is the solution to U x = b
        U must be an upper-triangular matrix
        b must be a vector of the same leading dimension as U
        """
        n, _ = L.get_size()
        x = Matrix.empty_row_array(n)

        U_elements = U.get_elements()
        b_elements = b.get_elements()

        for i in range(n-1, -1, -1):
            sum = b_elements[i]

            for j in range(i+1, n):
                sum -=  U_elements[i][j] * x[j]
            
            x[i] = sum / U_elements[i][i]

        return Matrix(x)

    def rank(self):
        rows, columns = self.get_size()
        j1 = min(rows, columns)

        for i in range(j1, 1, -1):
            if self.get_square_submatrices(i) != -1:
                return i
