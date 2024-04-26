class WordDictionary:

    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur:
                cur[c] = {}
            cur = cur[c]
        cur['*'] = ''

    def search(self, word: str) -> bool:

        def dfs(word, cur):
            if not word: 
                return True if '*' in cur else False
            c = word[0]
            if c in cur:
                return dfs(word[1:], cur[c])
            elif c == '.':
                for k in cur:
                    if dfs(word[1:], cur[k]): return True
            return False

        return dfs(word, self.root)
