
class Matrix:
    def __init__(self, elements):
        for i in elements:
            if len(i) != len(elements[0]):
                raise ValueError("Invalid row size")

        self.elements = elements

        self.rows = len(self.elements[0])
        self.columns = len(self.elements)

    def __str__(self):
        tmp = "\n"

        rows, _ = self.get_size()
        elements = self.get_elements()

        max_lengths = []
        for i in range(rows):
            column_lengths = [len(str(row[i])) for row in elements]
            max_lengths.append(max(column_lengths))

        for row in elements:
            tmp += "| "
            for i in range(rows):
                tmp += f"{str(row[i]):^{max_lengths[i]}} "
            tmp += "|\n"

        return tmp

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

    def transpose(self):
        elements = self.get_elements()
        rows, columns = self.get_size()

        transpose_matrix = [[0] * rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                transpose_matrix[j][i] = elements[i][j]

        return Matrix(transpose_matrix)

    def is_square(self):
        rows, columns = self.get_size()

        return rows == columns

    def minor(self, i, j):
        '''
        Extract a minor matrix by removing the ith row and jth column
        '''

        elements = self.get_elements()
        minor_elements = [row[:j] + row[j + 1:] for row_idx, row in enumerate(elements) if row_idx != i]

        return Matrix(minor_elements)

    def scalar_product(self, scalar):
        '''
        Multiply a matrix by a scalar
        '''

        elements = self.get_elements()
        rows, columns = self.get_size()

        for i in range(rows):
            for j in range(columns):
                elements[i][j] *= scalar

        return Matrix(elements)

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif Matrix.det(self) == 0:
            raise Exception("Matrix is not invertible")

        else:
            elements = self.get_elements()
            rows, _ = self.get_size()

            cof_elements = [[0] * rows for _ in range(rows)]

            for i in range(rows):
                for j in range(rows):
                    cof_elements[i][j] = elements[i][j] * ((-1) ** (i + j + 2)) * self.minor(i, j).det()

            cof_matrix = Matrix(cof_elements)

            return cof_matrix.scalar_product(1 / self.det())

    def det(self):
        if self.is_square():
            elements = self.get_elements()
            _, columns = self.get_size()            

            if columns == 1:
                return elements[0][0]

            elif columns == 2:
                return (elements[0][0] * elements[1][1]) - (elements[0][1] * elements[1][0])

            else:
                minors = [self.minor(0, j) for j in range(columns)]
                results = [minor.det() for minor in minors]

                return sum(results)

        else:
            raise ValueError("Cannot compute determinant of a non-square matrix")

    @staticmethod
    def product(A, B):
        a_rows, a_columns = A.get_size()
        _, b_columns = B.get_size()

        if a_rows != b_columns:
            raise ValueError("Number of columns of first matrix must match the number of rows of second matrix")

        else:
            a_elements = A.get_elements()
            b_elements = B.get_elements()

            result = [[[0] * i for i in range(b_columns)] for j in range(a_rows)]

            for i in range(a_rows):
                for j in range(b_columns):
                    result[i][j] = 0

                    for k in range(a_columns):
                        result[i][j] += a_elements[i][k] * b_elements[k][j]

        return Matrix(result)

    def get_square_submatrices(self, order):
        '''
        Auxiliary function for the rank()
        '''
        elements = self.get_elements()
        rows, columns = self.get_size()
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(columns - order + 1):
                submatrix = []
                
                for row in range(order):
                    submatrix.append(elements[start_row + row][start_col:start_col + order])
                
                submatrices.append(Matrix(submatrix))

        return submatrices

    def rank(self):
        j1 = min(self.size()['rows'], self.size()['columns'])

        for i in range(j1, 1, -1):
            if self.get_submatrices_rank(self, i) != -1:
                return i





