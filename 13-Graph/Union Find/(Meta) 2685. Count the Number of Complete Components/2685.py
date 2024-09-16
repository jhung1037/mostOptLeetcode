class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:

        par = [i for i in range(n)]
        size = [1] * n
        edge = [0] * n
        
        def find(n):
            p = par[n]
            while p != par[p]:
                p = par[p]
            return p

        def union(a, b):
            pa, pb = find(a), find(b)
            if pa != pb:
                if size[pa] >= size[pb]:
                    par[pb] = pa
                    size[pa] += size[pb]
                    edge[pa] += edge[pb]
                    edge[pa] += 1
                else:
                    par[pa] = pb
                    size[pb] += size[pa]
                    edge[pb] += edge[pa]
                    edge[pb] += 1
            else:
                edge[pa] += 1

        for e in edges:
            union(e[0],e[1])

        res = 0
        for i, p in enumerate(par):
            if i == p:
                if size[p] * (size[p]-1) // 2 == edge[p]:
                    res += 1
        return res
