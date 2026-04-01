class Solution:
    def isPalindrome(self, s: str) -> bool:
        # lowercase
        s = s.lower()
        # two pointers starting from each side of the string
        lptr, rptr = 0, len(s) - 1
        # palindrone if the two pointers cross each other
        while lptr < rptr:
            while lptr < rptr and not s[lptr].isalnum():
                lptr += 1
            while lptr < rptr and not s[rptr].isalnum():
                rptr -= 1
            if s[lptr] != s[rptr]:
                return False
            lptr += 1
            rptr -= 1
        return True