class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # time complexity = O(n)
        # space complexity = O(1)
        '''
        Only care for the number two indices before it to check if duplicated.
        '''
        k = 2
        for i in range(2, len(nums)):
            if nums[i] != nums[k-2]:
                nums[k] = nums[i]
                k += 1
        return k
