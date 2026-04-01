class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = res = 0
        counts = defaultdict(int)
        max_f = 0
        for r in range(len(s)):
            counts[s[r]] += 1
            max_f = max(max_f, counts[s[r]])

            while r - l + 1 - max_f > k:
                counts[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)

        return res