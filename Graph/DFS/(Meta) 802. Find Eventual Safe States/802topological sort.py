class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        adj = {i : set() for i in range(n)}
        outdegree = [0] * n
        for u, vs in enumerate(graph):
            for v in vs:
                adj[v].add(u)
                outdegree[u] += 1

        res = []
        for i, o in enumerate(outdegree):
            if o == 0:
                res.append(i)

        check = res.copy()
        while check:
            v = check.pop()
            for u in adj[v]:
                outdegree[u] -= 1
                if outdegree[u] != 0: continue
                res.append(u)
                check.append(u)

        return sorted(res)