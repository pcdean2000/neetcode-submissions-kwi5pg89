class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        cache = {}
        def dfs(l):
            if l == n:
                return True
            if l in cache:
                return cache[l]
            for r in range(l + 1, n + 1):
                if s[l : r] in wordDict and dfs(r):
                    cache[l] = True
                    return True
            cache[l] = False
            return False
        
        dfs(0)
        return cache[0]
            