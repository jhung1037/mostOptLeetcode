class Trie:
    def __init__(self):
        self.child = {}

    def add_sub(self, word):
        seen = []
        for i in range(len(word)):
            root = self.child
            for index, c in enumerate(word[i:]):
                if c in root and word[i:i+index+1] not in seen: root[c]['*'] += 1
                elif c not in root:
                    root[c] = {'*': 1}
                    seen.append(word[i:i+index+1])
                root = root[c]

    def bfs(self, word):
        root = self.child
        new = deque()
        for i, c in enumerate(word):
            new.append([i, i, root])

        while new:
            q = new.copy()
            new = deque()
            res = []
            while q:
                s, i, root = q.popleft()
                if i >= len(word): continue
                c = word[i]
                if c in root and root[c]['*'] == 1: res.append(word[s:i+1])
                elif c in root: new.append([s, i+1, root[c]])
            if res:
                return min(res)
        
        return ''


class Solution:
    def shortestSubstrings(self, arr: List[str]) -> List[str]:
        root = Trie()
        for a in arr:
            root.add_sub(a)

        res = []
        for a in arr:
            res.append(root.bfs(a))

        return res
        