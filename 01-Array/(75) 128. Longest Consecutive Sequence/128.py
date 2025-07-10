class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        res = 0
        hmap = set(nums)
        for num in hmap:
            if num-1 not in hmap:
                length = 1
                while num+length in hmap:
                    length += 1
                res = max(res, length)
        
        return res
