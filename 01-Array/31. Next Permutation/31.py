class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # time complexity = O(n)
        # space complexity = O(1)
        swap_index = -1
        for i in range(len(nums)-2,-1,-1):
            if nums[i] < nums[i+1]:
                swap_index = i
                break

        if swap_index != -1:
            for i in range(len(nums)-1,-1,-1):
                if nums[i] > nums[swap_index]:
                    nums[i] ^= nums[swap_index]
                    nums[swap_index] ^= nums[i]
                    nums[i] ^= nums[swap_index]
                    break

        for i in range((len(nums) - swap_index - 1) // 2):
            nums[i + swap_index + 1] ^= nums[len(nums)-1-i]
            nums[len(nums)-1-i] ^= nums[i + swap_index + 1]
            nums[i + swap_index + 1] ^= nums[len(nums)-1-i]

        return
