class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        
        for r in range(n // 2):
            matrix[r], matrix[n - 1 - r] = matrix[n - 1 - r], matrix[r]

        for r in range(0, n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
