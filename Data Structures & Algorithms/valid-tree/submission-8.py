class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # 要形成樹，|E| 一定是 |V| - 1
        if len(edges) != n - 1:
            return False

        # 建立 adjacent list 確保不會有遺漏的 edge
        adj_list = [[] for _ in range(n)]
        for u, v in edges:
            adj_list[u].append(v)
            adj_list[v].append(u)

        # 以 BFS 從 adjacent list [0] 開始走過所有節點
        # 用 visit set 記錄經過的節點
        # 重複訪問已經在 visit set 的節點代表存在環，不是樹，回傳 False
        q = deque()
        visit = set()
        q.append(0)
        while q:
            v = q.popleft()
            if v in visit:
                return False
            visit.add(v)
            for u in adj_list[v]:
                if u in visit:
                    continue
                q.append(u)

        # len(visit) < n 代表存在不只一個圖形，不是"一個樹"，回傳 False
        return len(visit) == n