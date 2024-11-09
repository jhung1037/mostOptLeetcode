class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # time complexity = O(nlogn)
        # space complexity = O(n)
        points.sort(key = lambda x: x[1])
        res = 0
        end = -math.inf
        for point in points:
            if point[0] > end:
                res += 1
                end = point[1]

        return res
