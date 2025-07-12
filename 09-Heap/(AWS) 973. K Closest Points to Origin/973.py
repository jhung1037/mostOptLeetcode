class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # time complexity: O(n)
        # space complexity: O(n)
        dis = []
        for x, y in points:
            dis.append(((x**2+y**2)**1/2, x, y))

        heapq.heapify(dis)

        res = []
        for i in range(k):
            _, x, y = heapq.heappop(dis)
            res.append([x, y])

        return res
