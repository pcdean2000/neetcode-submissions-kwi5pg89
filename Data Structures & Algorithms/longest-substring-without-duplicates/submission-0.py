class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = res = 0
        seen = set()
        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            seen.add(s[r])
            res = max(res, len(seen))
        
        return res