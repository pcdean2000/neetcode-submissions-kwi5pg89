class Solution:
    def longestPalindrome(self, s: str) -> str:
        def helper(l, r):
            max_str = ""
            while 0 <= l and r < len(s) and s[l] == s[r]:
                if r - l + 1 > len(max_str):
                    max_str = s[l:r + 1]
                l -= 1
                r += 1
            return max_str
        
        res = ""
        for i in range(len(s)):
            # odd
            cur_odd = helper(i, i)

            # even
            cur_even = helper(i, i + 1)

            if len(cur_even) > len(cur_odd):
                cur_str = cur_even
            else:
                cur_str = cur_odd
            
            if len(cur_str) > len(res):
                res = cur_str

        return res
        