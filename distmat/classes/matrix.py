from mat import base_ops as bm


class Matrix:
    def __init__(self, elements):
        for i in elements:
            if len(i) != len(elements[0]):
                raise ValueError("Invalid row size")

        self.elements = elements

    def __str__(self):
        tmp = "\n"

        max_lengths = []
        for i in range(len(self.elements[0])):
            column_lengths = [len(str(row[i])) for row in self.elements]
            max_lengths.append(max(column_lengths))

        for row in self.elements:
            tmp += "| "
            for i in range(len(self.elements[0])):
                tmp += f"{str(row[i]):^{max_lengths[i]}} "
            tmp += "|\n"

        return tmp

    def size(self):
        rows = len(self.elements)
        columns = len(self.elements[0])

        return {"rows": rows, "columns": columns}

    def get(self):
        return self.elements

    def transpose(self):
        a = self.get()
        rows = self.size()["rows"]
        columns = self.size()["columns"]

        transpose_matrix = [[0] * rows for _ in range(columns)]

        for i in range(rows):
            for j in range(columns):
                transpose_matrix[j][i] = a[i][j]

        return Matrix(transpose_matrix)

    def is_square(self):
        return self.size()["rows"] == self.size()["columns"]

    def minor(self, i, j):
        minor_elements = [row[:j] + row[j + 1:] for row_idx, row in enumerate(self.elements) if row_idx != i]
        return Matrix(minor_elements)

    def scalar_product(self, scalar):
        elems = self.get()

        rows = self.size()['rows']
        cols = self.size()['columns']

        for i in range(rows):
            for j in range(cols):
                elems[i][j] *= scalar

        return Matrix(elems)

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")

        elif Matrix.det(self) == 0:
            raise Exception("Matrix is not invertible")

        else:
            size = self.size()["rows"]
            a = self.get()
            cof_arr = [[0] * size for _ in range(size)]

            for i in range(size):
                for j in range(size):
                    cof_arr[i][j] = a[i][j] * ((-1) ** (i + j + 2)) * self.minor(i, j).det()

            cof_matrix = Matrix(cof_arr)

            return cof_matrix.scalar_product(1 / self.det())

    def det(self):
        if self.is_square():
            cols = self.size()["columns"]
            elements = self.get()

            if cols == 1:
                return elements[0][0]

            elif cols == 2:
                return (elements[0][0] * elements[1][1]) - (elements[0][1] * elements[1][0])

            else:
                submatrices = [self.minor(0, j) for j in range(cols)]
                results = [submatrix.det() for submatrix in submatrices]

                return sum(results)

        else:
            raise ValueError("Cannot compute determinant of a non-square matrix")

    def product(self, b):
        a_columns = self.size()["columns"]
        a_rows = self.size()["rows"]

        b_columns = b.size()["columns"]
        b_rows = b.size()["rows"]

        if a_rows != b_columns:
            raise ValueError("Number of columns of first matrix must match the number of rows of second matrix")

        else:
            a = self.get()
            b = b.get()

            result = [[[0] * i for i in range(b_columns)] for j in range(a_rows)]

            for i in range(a_rows):
                for j in range(b_columns):
                    result[i][j] = 0
                    for k in range(a_columns):
                        result[i][j] += a[i][k] * b[k][j]

        return Matrix(result)

    def get_square_submatrices(self, order):
        rows = self.size()["rows"]
        cols = self.size()["columns"]
        submatrices = []

        for start_row in range(rows - order + 1):
            for start_col in range(cols - order + 1):
                submatrix = []
                
                for row in range(order):
                    submatrix.append(self.elements[start_row + row][start_col:start_col + order])
                submatrices.append(Matrix(submatrix))

        return submatrices

    def rank(self):
        j1 = min(self.size()['rows'], self.size()['columns'])

        for i in range(j1, 1, -1):
            if bm.get_submatrices_rank(self, i) != -1:
                return i





