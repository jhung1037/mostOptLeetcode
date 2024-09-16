class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(s, l, r):
            if l == r == n:
                res.append(s)
                return
            if l < n:
                dfs(s + '(', l+1, r)
            if l > r:
                dfs(s + ')', l, r+1)
            return
        
        dfs('',0,0)
        return res
