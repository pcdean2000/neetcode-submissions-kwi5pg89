class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        ROW, COL = len(matrix), len(matrix[0])
        zeroes = []
        # Collect all zero positions
        for r in range(ROW):
            for c in range(COL):
                if matrix[r][c] == 0:
                    zeroes.append((r, c))
        # Simulate the action described in the question
        for R, C in zeroes:
            # Replace row
            for r in range(ROW):
                matrix[r][C] = 0
            # Replace column
            for c in range(COL):
                matrix[R][c] = 0