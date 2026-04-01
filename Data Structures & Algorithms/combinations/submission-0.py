class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(i, cur_comb):
            if len(cur_comb) == k:
                res.append(cur_comb.copy())
                return
            
            for j in range(i, n):
                cur_comb.append(j + 1)
                dfs(j + 1, cur_comb)
                cur_comb.pop()
        
        res = []
        dfs(0, [])
        return res