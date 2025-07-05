class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        # time complexity = O(n)
        # space complexity = O(1)

        if len(nums) < 3: return 0
        res = 0
        a = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                a+=1
                res+=a
            else:
                a = 0

        return res
