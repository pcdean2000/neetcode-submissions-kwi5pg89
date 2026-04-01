class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def is_row_valid():
            for row in board:
                seen = set()
                for n in row:
                    if not n.isdigit():
                        continue
                    if n in seen:
                        return False
                    seen.add(n)
            return True
        
        def is_col_valid():
            for c in range(9):
                seen = set()
                for r in range(9):
                    if not board[r][c].isdigit():
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
            return True

        def is_block_valid():
            for br in [0, 3, 6]:
                for bc in [0, 3, 6]:
                    seen = set()
                    for r in range(br, br + 3):
                        for c in range(bc, bc + 3):
                            if not board[r][c].isdigit():
                                continue
                            if board[r][c] in seen:
                                return False
                            seen.add(board[r][c])
            return True
        
        return is_row_valid() and is_col_valid() and is_block_valid()
