class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(r, c, i):
            if board[r][c] != word[i]:
                return False
            if i == n - 1:
                return True
            seen.add((r, c))
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if ((nr, nc) in seen or
                    not 0 <= nr < ROW or
                    not 0 <= nc < COL):
                    continue
                if dfs(nr, nc, i + 1):
                    return True
            seen.remove((r, c))
            return False
        
        ROW, COL = len(board), len(board[0])
        n = len(word)
        dirs = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]
        for r in range(ROW):
            for c in range(COL):
                seen = set()
                if dfs(r, c, 0):
                    return True
        return False