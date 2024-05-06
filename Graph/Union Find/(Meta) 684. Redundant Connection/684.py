class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        anc = {}
        for edge in edges:
            u, v = edge
            while u in anc:
                u = anc[u]
            while v in anc:
                v = anc[v]
            if u == v: return edge
            if u < v:
                anc[v] = u
            else:
                anc[u] = v
