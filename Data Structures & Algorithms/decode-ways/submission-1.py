class Solution:
    def numDecodings(self, s: str) -> int:
        prev2_count = 0
        prev1_count = 1
        prev_char = ""
        for c in s:
            current = 0
            if c != '0':
                current += prev1_count
            if 10 <= int(prev_char + c) <= 26:
                current += prev2_count
            prev_char = c
            prev2_count = prev1_count
            prev1_count = current
        return prev1_count
            