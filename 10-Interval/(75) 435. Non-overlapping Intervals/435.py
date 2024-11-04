class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # time complexity = O(nlogn)
        # space complexity = O(n)
        '''
        Only have to mind the end element of each interval.
        '''
        intervals.sort(key = lambda x: x[1])
        end = -math.inf
        remove = 0
        for interval in intervals:
            if interval[0] < end:
                remove += 1
            else:
                end = interval[1]
        
        return remove
