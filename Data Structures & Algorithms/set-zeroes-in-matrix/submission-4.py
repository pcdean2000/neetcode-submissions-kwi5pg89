class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        def print_matrix():
            for r in range(ROW):
                for c in range(COL):
                    print(f"{matrix[r][c]:^3}", end=" ")
                print()
            print()
        
        ROW, COL = len(matrix), len(matrix[0])

        print_matrix()

        # Check if the first row and the first column have zero
        zero_row = zero_col = False
        for r in range(ROW):
            if matrix[r][0] == 0:
                zero_col = True
                break
        for c in range(COL):
            if matrix[0][c] == 0:
                zero_row = True
                break
        
        # Turn the first row and the first column into 0
        # as a mark when encounter an 0 in the matrix
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    matrix[0][c] = 0
                
        print_matrix()
        
        # Walthrough the first row and the first column
        # turn the entire row or column into 0 when 0 appears
        for r in range(1, ROW):
            for c in range(1, COL):
                if matrix[0][c] == 0 or matrix[r][0] == 0:
                    matrix[r][c] = 0

        print_matrix()

        # Turn the first row and the first column into 0 accordingly
        if zero_row:
            for c in range(COL):
                matrix[0][c] = 0
        if zero_col:
            for r in range(ROW):
                matrix[r][0] = 0