class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase
        s = s.lower()
        # remove non-alphanumeric
        s_alnum = ""
        for c in s:
            if not c.isalnum():
                continue
            s_alnum += c
        # two pointers starting from each side of the string
        lptr, rptr = 0, len(s_alnum) - 1
        # palindrone if the two pointers cross each other
        while lptr < rptr:
            if s_alnum[lptr] != s_alnum[rptr]:
                return False
            lptr += 1
            rptr -= 1
        return True