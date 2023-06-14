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
        if self.size["rows"] != self.size["columns"]:
            raise Exception("Matrix must be square")
        
    def det(self):
        pass

    def lu_decomp(self):
        n = self.size()["rows"]
        L = U = [[0.0] * n for _ in range(n)]

        for i in range(n):
            L[i][i] = 1.0

        for j in range(n):
            for i in range(j, n):
                sum_upper = sum(L[i][k] * U[k][j] for k in range(j))
                U[i][j] = self.elements[i][j] - sum_upper

            for i in range(j, n):
                sum_lower = sum(L[i][k] * U[k][j] for k in range(j))
                L[i][j] = (self.elements[i][j] - sum_lower) / U[j][j]

        return L, U



A = Matrix(
    [[1,2], 
     [3,4]]
     )
     
print(A)
L, U = A.lu_decomp()
