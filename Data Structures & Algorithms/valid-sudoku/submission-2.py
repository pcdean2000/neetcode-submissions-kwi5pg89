class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]

        blocks = [
            [
                set() for _ in range(3)
            ]
            for _ in range(3)
        ]

        for r in range(9):
            for c in range(9):
                if not board[r][c].isdigit():
                    continue
                if board[r][c] in rows[r] \
                or board[r][c] in cols[c] \
                or board[r][c] in blocks[r // 3][c // 3]:
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                blocks[r // 3][c // 3].add(board[r][c])

        return True
