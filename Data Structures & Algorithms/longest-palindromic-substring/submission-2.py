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
            l, r = helper(i, i)
            if r - l + 1 > len(res):
                res = s[l : r + 1]

            # even
            l, r = helper(i, i + 1)
            if r - l + 1 > len(res):
                res = s[l : r + 1]

        return res
        