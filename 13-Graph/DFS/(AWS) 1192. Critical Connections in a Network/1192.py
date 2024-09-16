class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        
        graph = collections.defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)

        low = [-1] * n
        def dfs(v, par, lvl):
            low[v] = lvl
            for child in graph[v]:
                if child == par:
                    continue
                elif low[child] != -1:
                    low[v] = min(low[v], low[child])
                else:
                    low[v] = min(low[v], dfs(child, v, lvl+1))
            if low[v] == lvl and v != 0:
                res.append([par, v])
            return low[v]

        res = []
        dfs(0,-1, 1)
        return res