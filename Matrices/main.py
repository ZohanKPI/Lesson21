class Matrix:
    def __init__(self, lists):
        self.matrix = lists
    def print_default_matrix(self):
        for row in self.matrix:
            print(row)
    def print_matrix(self, matrix=None):
        matrix_to_print = self.matrix if matrix is None else matrix
        for row in matrix_to_print:
            print(row)
    def add(self, other_matrix):
        if len(other_matrix.matrix) != len(self.matrix) or len(other_matrix.matrix[0]) != len(self.matrix[0]):
            raise ValueError("Sizes don't match!")
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other_matrix.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def subtract(self, other_matrix):
        if len(self.matrix) != len(other_matrix.matrix) or len(self.matrix[0]) != len(other_matrix.matrix[0]):
            raise ValueError("Sizes don't match!")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other_matrix.matrix[i][j])
            result.append(row)

        return Matrix(result)

    def multiply_number(self, number):
        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] * number)
            result.append(row)

        return Matrix(result)

    def multiply_matrix(self, other_matrix):
        if len(self.matrix[0]) != len(other_matrix.matrix):
            raise ValueError("Sizes don't match!")

        result = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(other_matrix.matrix[0])):
                cell = sum([self.matrix[i][k] * other_matrix.matrix[k][j] for k in range(len(self.matrix[0]))])
                row.append(cell)
            result.append(row)

        return Matrix(result)

    def transpose(self):
        result = [[self.matrix[j][i] for j in range(len(self.matrix))] for i in range(len(self.matrix[0]))]
        return Matrix(result)

matrix_data1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix1 = Matrix(matrix_data1)

matrix_data2 = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

matrix2 = Matrix(matrix_data2)

print("Matrix 1 by default:")
matrix1.print_default_matrix()
print("Matrix 2 by default:")
matrix2.print_default_matrix()

print("After addition:")
result = matrix1.add(matrix2)
result.print_matrix()

print("After subtraction:")
result = matrix1.subtract(matrix2)
result.print_matrix()

print("After multiplication by 3:")
result = matrix1.multiply_number(3)
result.print_matrix()

print("After multiplication by matrix 2:")
result = matrix1.multiply_matrix(matrix2)
result.print_matrix()

print("After transposition:")
result = matrix1.transpose()
result.print_matrix()
#2
matrix = [[4, 2, 0], [1, 3, 2], [-1, 3, 10]]

matrix[0], matrix[1] = matrix[1], matrix[0]
for i in range(len(matrix[0])):
    matrix[1][i] += -4 * matrix[0][i]
    matrix[2][i] += matrix[0][i]
for i in range(len(matrix[1])):
    matrix[1][i] /= -2
    matrix[2][i] /= 6
matrix[1], matrix[2] = matrix[2], matrix[1]
for i in range(len(matrix[1])):
    matrix[2][i] += -5 * matrix[1][i]
print("Transformed matrix:")
for row in matrix:
    print(row)