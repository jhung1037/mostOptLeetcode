class WordDictionary:

    def __init__(self):
        self.ref = {}

    def addWord(self, word: str) -> None:
        curr = self.ref
        for c in word:
            if c not in curr:
                curr[c] = {}
            curr = curr[c]
        curr['*'] = None

    def search(self, word: str) -> bool:
        
        def dfs(i, curr):
            if i == len(word):
                return '*' in curr
            if word[i] == '.':
                for c in curr:
                    if c == '*': continue
                    if dfs(i+1, curr[c]):
                        return True
            elif word[i] in curr:
                return dfs(i+1, curr[word[i]])
            return False

        return dfs(0, self.ref)
