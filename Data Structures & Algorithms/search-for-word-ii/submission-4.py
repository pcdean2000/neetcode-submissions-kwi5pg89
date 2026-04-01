class TrieNode:
    def __init__(self) -> None:
        self.characters = {}
        self.word = ""

class Dictionary:
    def __init__(self) -> None:
        self.root = TrieNode()
    
    def insert(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
        cur.word = word

    def get_root(self) -> TrieNode:
        return self.root

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(node, r, c):
            if (not 0 <= r < ROW or
                not 0 <= c < COL or
                board[r][c] not in node.characters or
                (r, c) in visit):
                return
            next_node = node.characters[board[r][c]]
            if next_node.word:
                res.append(next_node.word)
                next_node.word = ""
            visit.add((r, c))
            dfs(next_node, r - 1, c)
            dfs(next_node, r + 1, c)
            dfs(next_node, r, c - 1)
            dfs(next_node, r, c + 1)
            visit.remove((r, c))
            if not next_node.characters:
                node.characters.pop(board[r][c])

        word_bank = Dictionary()
        for word in words:
            word_bank.insert(word)
        
        ROW, COL = len(board), len(board[0])
        root = word_bank.get_root()
        res = []
        visit = set()
        for r in range(ROW):
            for c in range(COL):
                dfs(root, r, c)
        
        return res