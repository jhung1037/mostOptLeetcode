class Trie:
    def __init__(self):
        self.subfile = {}
        self.end = False

class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        dummy = root = Trie()
        res = []

        for f in folder:
            root = dummy
            for filename in f[1:].split('/'): # f[1:] or else it would '/a' would be -> '' & 'a'
                if filename not in root.subfile: root.subfile[filename] = Trie()
                root = root.subfile[filename]
            root.end = True
        
        def dfs(root, res, append):
            for filename in root.subfile:
                if root.subfile[filename].end:
                    res.append(append + "/" + filename)
                    continue
                dfs(root.subfile[filename], res, append + "/" + filename)

        dfs(dummy,res,"")
        return res
