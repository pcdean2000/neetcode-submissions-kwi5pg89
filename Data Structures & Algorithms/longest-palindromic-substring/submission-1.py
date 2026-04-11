class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            max_length = 0
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > max_length:
                    max_length = r - l + 1
                l -= 1
                r += 1
            return l + 1, r - 1
        
        res = ""
        for i in range(len(s)):
            # odd
            odd_l, odd_r = helper(i, i)

            # even
            even_l, even_r = helper(i, i + 1)

            l = min(odd_l, even_l)
            r = max(odd_r, even_r)

            if r - l + 1 > len(res):
                res = s[l : r + 1]

        return res
        