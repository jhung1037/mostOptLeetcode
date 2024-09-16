class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curr = 0
        for num in nums:
            curr += num
            if curr > res:
                res = curr
            if curr < 0:
                curr = 0
        return res
