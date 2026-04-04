class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def dfs(i, cur):
            if i == len(digits):
                res.append("".join(cur))
                return
            
            for c in digit_map[digits[i]]:
                cur.append(c)
                dfs(i + 1, cur)
                cur.pop()
        
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        dfs(0, [])

        return res