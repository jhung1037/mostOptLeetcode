class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        adj = [[] for _ in range(n)]
        for rich, poor in richer:
            adj[poor].append(rich)

        def dfs(poor):
            if res[poor] == -1:
                res[poor] = poor
                for rich in adj[poor]:
                    dfs(rich)
                    res[poor] = min(res[rich], res[poor], key = lambda x: quiet[x])
                
        
        res = [-1] * n
        for i in range(n):
            dfs(i)
        return res