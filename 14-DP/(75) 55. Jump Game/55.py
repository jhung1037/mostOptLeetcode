class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # time complexity: O(n)
        # space complexity: O(1)
        if 0 not in nums or len(nums) == 1: return True

        goal = len(nums) - 1
        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= goal:
                goal = i
        
        return goal == 0
