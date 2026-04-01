class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n_row, n_col = len(matrix), len(matrix[0])
        self.accu_matrix = [[0] * (n_col + 1) for _ in range(n_row + 1)]
        for r in range(n_row):
            for c in range(n_col):
                self.accu_matrix[r + 1][c + 1] = matrix[r][c] \
                                               + self.accu_matrix[r + 1][c] \
                                               + self.accu_matrix[r][c + 1] \
                                               - self.accu_matrix[r][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.accu_matrix[row2 + 1][col2 + 1] \
             - self.accu_matrix[row1][col2 + 1] \
             - self.accu_matrix[row2 + 1][col1] \
             + self.accu_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)