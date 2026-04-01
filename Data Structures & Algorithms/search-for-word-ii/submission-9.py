class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(parent_node, r, c):
            if (not 0 <= r < ROW or
                not 0 <= c < COL or
                board[r][c] not in parent_node):
                return
            char = board[r][c]
            curr_node = parent_node[char]

            word = curr_node.pop("$", None)
            if word:
                res.add(word)

            board[r][c] = "#"
            dfs(curr_node, r - 1, c)
            dfs(curr_node, r + 1, c)
            dfs(curr_node, r, c - 1)
            dfs(curr_node, r, c + 1)
            board[r][c] = char

            if not curr_node:
                parent_node.pop(char)

        trie = {}
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node["$"] = word
        
        ROW, COL = len(board), len(board[0])
        res = set()
        for r in range(ROW):
            for c in range(COL):
                dfs(trie, r, c)
        
        return list(res)