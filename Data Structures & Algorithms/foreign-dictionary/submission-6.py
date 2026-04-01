class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # 從兩個字中找到不一樣的字元 (w1, w2 順序 = 前後關係)
        def get_edge(w1, w2):
            for i in range(min(len(w1), len(w2))):
                if w1[i] != w2[i]:
                    return [w1[i], w2[i]]
            # 如果出現第一個字比第二個字長 (e.g. fore, for)，代表有問題
            if len(w1) > len(w2):
                return None
            # 第二個字是第一個字的擴展 (e.g. for, fore)，無從比較前後關係，回傳空
            return []
        
        # 記錄所有出現過的字元，避免沒有 edge 的字元被遺漏
        alphabet = set()
        for w in words:
            alphabet.update(list(w))

        # 建立 adjacent list 和 indegree
        # adj = {"pre": [post]}
        # indegree = {"post": #pre}
        adj = defaultdict(set)
        indegree = {alpha: 0 for alpha in alphabet}
        for i in range(1, len(words)):
            edge = get_edge(words[i - 1], words[i])
            if edge is None:
                return ""
            if not edge:
                continue
            if edge[1] not in adj[edge[0]]:
                adj[edge[0]].add(edge[1])
                indegree[edge[1]] += 1
        
        # 使用 Kahn's algo 遍歷所有的 alpha
        q = deque()
        for alpha, degree in indegree.items():
            if degree == 0:
                q.append(alpha)
        
        topo = []
        while q:
            alpha = q.popleft()
            topo.append(alpha)
            for post in adj[alpha]:
                indegree[post] -= 1
                if indegree[post] == 0:
                    q.append(post)
        
        # 最終檢查 topo 長度對不對
        if len(topo) != len(alphabet):
            return ""
        
        return "".join(topo)