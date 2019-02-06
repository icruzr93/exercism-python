class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = [[int(col) for idc, col in enumerate(row.split(' '))] for idr, row in enumerate(matrix_string.split('\n'))]

    def row(self, index):
        return self.matrix[index - 1]

    def column(self, index):
        return [row[index-1] for row in self.matrix]
