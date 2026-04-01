class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(heights), len(heights[0])
        flow = [
            [
                0
                for _ in range(COL)
            ]
            for _ in range(ROW)
        ]
        def climb(loc, visited : List[List[bool]]):
            r, c = loc
            if visited[r][c]:
                return
            flow[r][c] += 1
            visited[r][c] = True
            if 0 < r and heights[r][c] <= heights[r - 1][c]:       climb((r - 1, c), visited)
            if r < ROW - 1 and heights[r][c] <= heights[r + 1][c]: climb((r + 1, c), visited)
            if 0 < c and heights[r][c] <= heights[r][c - 1]:       climb((r, c - 1), visited)
            if c < COL - 1 and heights[r][c] <= heights[r][c + 1]: climb((r, c + 1), visited)
        
        def climb_pacific():
            visited = [
                [
                    False
                    for _ in range(COL)
                ]
                for _ in range(ROW)
            ]
            for r in range(ROW):
                climb((r, 0), visited)
            for c in range(1, COL):
                climb((0, c), visited)
        
        def climb_alantic():
            visited = [
                [
                    False
                    for _ in range(COL)
                ]
                for _ in range(ROW)
            ]
            for r in range(ROW):
                climb((r, COL - 1), visited)
            for c in range(COL - 1):
                climb((ROW - 1, c), visited)
        
        climb_pacific()
        climb_alantic()

        res = []
        for r in range(ROW):
            for c in range(COL):
                if flow[r][c] == 2:
                    res.append([r, c])
        
        return res