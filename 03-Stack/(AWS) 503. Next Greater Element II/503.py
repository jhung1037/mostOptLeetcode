class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # time complexity: O(n)
        # space complexity: O(n)
        stack = []
        res = [-1] * len(nums)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]
            stack.append(i)
        for i in range(len(nums)):
            while stack and nums[i] > nums[stack[-1]]:
                res[stack.pop()] = nums[i]

        return res
