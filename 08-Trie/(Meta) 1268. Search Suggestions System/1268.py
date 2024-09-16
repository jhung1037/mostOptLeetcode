class TrieNode:
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.suggestions = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            curr = curr.children[c]
            if len(curr.suggestions) < 3:
                curr.suggestions.append(word)

    def search(self, word):
        curr = self.root
        res = []
        for c in word:
            curr = curr.children[c]
            res.append(curr.suggestions)

        return res

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        dic = Trie()
        products.sort()
        for product in products:
            dic.add(product)

        return dic.search(searchWord)
