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
        if self.is_square:
            raise Exception("Matrix must be square")
        
    def is_square(self):
        return self.size["rows"] == self.size["columns"]
                
    def minor(self, i, j):
        minor_elements = [row[:j] + row[j+1:] for row_idx, row in enumerate(self.elements) if row_idx != i]
        return Matrix(minor_elements)


def det(A):
    if A.is_square():
        size = A.size()["rows"]
        
        if size <= 2:
            pass

        else:
            sum = 0
            i = 0

            for j in range(0, size):
                A.get()[i][j] * (-1 ** (i + j)) * det(A.minor(i, j))

A = Matrix(
    [[1,2], 
     [3,4]]
     )
     
print(A)
