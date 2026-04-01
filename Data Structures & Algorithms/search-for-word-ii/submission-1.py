class TrieNode:
    def __init__(self) -> None:
        self.characters = {}
        self.word = False

class Dictionary:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
        cur.word = True

    def get_root(self) -> TrieNode:
        return self.root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, r, c, prefix):
            if (not 0 <= r < ROW or
                not 0 <= c < COL or
                board[r][c] not in node.characters or
                (r, c) in visit):
                return
            prefix += board[r][c]
            next_node = node.characters[board[r][c]]
            if next_node.word:
                res.append(prefix)
                next_node.word = False
            visit.add((r, c))
            dfs(next_node, r - 1, c, prefix)
            dfs(next_node, r + 1, c, prefix)
            dfs(next_node, r, c - 1, prefix)
            dfs(next_node, r, c + 1, prefix)
            visit.remove((r, c))

        word_bank = Dictionary()
        for word in words:
            word_bank.insert(word)
        
        ROW, COL = len(board), len(board[0])
        root = word_bank.get_root()
        res = []
        visit = set()
        for r in range(ROW):
            for c in range(COL):
                visit.clear()
                dfs(root, r, c, "")
        
        return res