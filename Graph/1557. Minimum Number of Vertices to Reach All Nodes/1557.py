class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        return {i for i in range(n)} - set([edge[1] for edge in edges])
