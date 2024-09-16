class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        heap = []
        for i, row in enumerate(mat):
            count = 0
            for col in row:
                if not col: break
                count += 1
            heapq.heappush(heap,(count, i))

        ans = []
        for j in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans
