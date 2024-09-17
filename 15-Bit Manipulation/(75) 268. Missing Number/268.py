class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # time complexity = O(n)
        # space complexity = O(1)
        '''
        Find the missing number by deducting the sum of the numbers that are supposed to appear.
        Similarly, use XOR to eliminate the numbers that appear twice.
        '''
        missing = len(nums)
        for i in range(len(nums)):
            missing ^= i ^ nums[i]
        return missing
