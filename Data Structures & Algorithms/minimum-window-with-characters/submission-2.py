class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        s_freq, t_freq = defaultdict(int), defaultdict(int)
        for c in t:
            t_freq[c] += 1
        
        l = have = 0
        res_len = float("inf")
        res_indices = [-1, -1]
        for r, c in enumerate(s):
            s_freq[c] += 1
            if c in t_freq and s_freq[c] == t_freq[c]:
                have += 1
            while have == len(t_freq):

                if r - l + 1 < res_len:
                    res_len = r - l + 1
                    res_indices = [l, r]

                left_c = s[l]
                if left_c in t_freq and s_freq[left_c] == t_freq[left_c]:
                    have -= 1
                s_freq[left_c] -= 1
                l += 1
        
        l, r = res_indices
        return s[l:r + 1] if res_len != float("inf") else ""