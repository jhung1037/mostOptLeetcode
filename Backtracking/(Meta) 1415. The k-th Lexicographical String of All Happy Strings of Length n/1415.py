class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def dfs(s, lc):
            nonlocal k
            if len(s) == n:
                k -= 1
                if k == 0:
                    return s
                return

            for c in ["a", "b", "c"]:
                if lc != c:
                    if res:= dfs(s+c, c):
                        return res
            
            return ''

        return dfs('', '')
