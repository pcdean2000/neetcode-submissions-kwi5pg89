class TrieNode:
    def __init__(self) -> None:
        self.characters = {}
        self.word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.characters:
                cur.characters[c] = TrieNode()
            cur = cur.characters[c]
        cur.word = True

    def search(self, word: str) -> bool:
        cur = self.root
        n = len(word)
        def dfs(start, cur):
            for i in range(start, n):
                if word[i] == ".":
                    return any((dfs(i + 1, remain) for _, remain in cur.characters.items()))
                if word[i] not in cur.characters:
                    return False
                cur = cur.characters[word[i]]
            return cur.word
        return dfs(0, cur)
