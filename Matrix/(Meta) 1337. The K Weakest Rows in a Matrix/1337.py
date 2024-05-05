class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            heapq.heappush(heap, (sum(row),i))
            
        ans = []
        for j in range(k):
            _, i = heapq.heappop(heap)
            ans.append(i)
        return ans
