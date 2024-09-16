class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for i, point in enumerate(points):
            d = point[0] ** 2 + point[1] ** 2
            heapq.heappush(heap, (d,i))

        return [points[heapq.heappop(heap)[1]] for _ in range(k)]