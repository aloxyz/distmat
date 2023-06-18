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

    def inv(self):
        if not self.is_square():
            raise Exception("Matrix must be square")
        
        elif det(self) == 0:
            raise Exception("Matrix is not invertible")
        
        else:
            size = A.size()["rows"]
            a = A.get()
            cof_arr = []

            for i in range(size):
                for j in range(size):
                    cof_arr[i][j] = a[i][j] * ((-1) ** (i + j + 2)) * det(A.minor(i, j))

            cof_matrix = Matrix(cof_arr)

            # return (1/det(self)) * cof_matrix

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
        minor_elements = [row[:j] + row[j+1:] for row_idx, row in enumerate(self.elements) if row_idx != i]
        return Matrix(minor_elements)

def det(A):
    if A.is_square():
        size = A.size()["rows"]
        a = A.get()

        if size == 1:
            return a[0][0]

        elif size == 2:
            return (a[0][0] * a[1][1]) - (a[0][1] * a[1][0])

        else:
            for i in range(size):
                sum = 0

                for j in range(size):
                    sum += a[i][j] * ((-1) ** (i + j + 2)) * det(A.minor(i, j))

            return sum

def product(A, B):
    a_columns = A.size()["columns"];
    a_rows = A.size()["rows"]

    b_columns = B.size()["columns"]
    b_rows = B.size()["rows"];

    if a_columns != b_rows:
        raise ValueError("Number of columns of first matrix must match the number of rows of second matrix")

    else:
        a = A.get()
        b = B.get()

        result = [[0] * a_rows for _ in range(b_columns)]


        for i in range(a_rows):
            for j in range(b_columns):
                result[i][j] = a[i]

                


A = Matrix(
    [[1,2,3,4], 
     [3,4,5,6],
     [6,7,8,7],
     [8,9,0,1]]
     )
     
print(A)
print(det(A))
print(A.transpose())

