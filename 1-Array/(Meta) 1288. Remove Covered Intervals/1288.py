class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        c = d = -1
        res = 0
        for a, b in intervals:
            if a > c and b > d:
                res += 1
                c = a
            d = max(b,d)

        return res
