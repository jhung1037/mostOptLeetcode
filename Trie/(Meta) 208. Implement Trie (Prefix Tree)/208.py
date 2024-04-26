class Trie:

    def __init__(self):
        self.child = {}
        self.end = False

    def insert(self, word: str) -> None:
        for c in word:
            if c not in self.child:
                self.child[c] = Trie()
            self = self.child[c]
        self.end = True

    def search(self, word: str) -> bool:
        for c in word:
            if c not in self.child:
                return False
            self = self.child[c]
        return True if self.end else False

    def startsWith(self, prefix: str) -> bool:
        for c in prefix:
            if c not in self.child:
                return False
            self = self.child[c]
        return True
