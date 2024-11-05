class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # time complexity = O(nlogn)
        # space complexity = O(n)
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            if res[-1][1] < intervals[i][0]:
                res.append(intervals[i])
            else:
                res[-1][1] = max(res[-1][1], intervals[i][1])
        return res
