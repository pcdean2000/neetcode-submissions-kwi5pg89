class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right, top, bottom = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while left <= right and top <= bottom:
            
            # top-left to top-right
            for c in range(left, right + 1):
                res.append(matrix[top][c])
            top += 1
            if top > bottom:
                break
            
            # top-right to bottom-right
            for r in range(top, bottom + 1):
                res.append(matrix[r][right])
            right -= 1
            if left > right:
                break

            # bottom-right to bottom-left
            for c in range(right, left - 1, -1):
                res.append(matrix[bottom][c])
            bottom -= 1
            if top > bottom:
                break

            # bottom-left to top-left
            for r in range(bottom, top - 1, -1):
                res.append(matrix[r][left])
            left += 1
            if left > right:
                break
        
        return res
