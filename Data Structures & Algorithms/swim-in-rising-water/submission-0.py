class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        heap_loc = []
        heapq.heappush(heap_loc, (grid[0][0], (0, 0)))
        visit = set()
        cur_time = 0
        while heap_loc:
            t, pos = heapq.heappop(heap_loc)
            if pos in visit:
                continue
            cur_time = max(cur_time, t)
            if pos == (ROW - 1, COL - 1):
                break
            r, c = pos
            next_pos = [
                (r - 1, c),
                (r + 1, c),
                (r, c - 1),
                (r, c + 1),
            ]
            for nr, nc in next_pos:
                if (not (0 <= nr < ROW and 0 <= nc < COL) or
                    (nr, nc) in visit):
                    continue
                heapq.heappush(heap_loc, (grid[nr][nc], (nr, nc)))
            visit.add(pos)
        return cur_time