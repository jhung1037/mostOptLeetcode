class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        count = Counter(nums)
        res = 0
        
        if k == 0:
            for value in count.values():
                if value > 1:
                    res += 1
        else:
            for key in count:
                if key + k in count:
                    res += 1

        return res
