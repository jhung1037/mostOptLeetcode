class Solution:
    def rob(self, nums: List[int]) -> int:
        # time complexity = O(n)
        # space complexity = O(1)
        '''
        Do two iterations. One with the first house, the other with the last house.
        '''
        if len(nums) <= 2: return max(nums)
        
        def dp(nums):
            res = rob1 = rob2 = 0

            for num in nums:
                res = max(rob1, rob2 + num)
                rob2 = rob1
                rob1 = res
            
            return res
        
        return max(dp(nums[:-1]), dp(nums[1:]))
