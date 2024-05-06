class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        par = [i for i in range(n)]

        def find(i):
            while i != par[i]:
                i = par[i]
            return i
        
        def union(i, j):
            i, j = find(i), find(j)
            if i == j:
                return False
            else:
                par[j] = i
                return True

        for edge in edges:
            if not union(*edge):
                return edge
