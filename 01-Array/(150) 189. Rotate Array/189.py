class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # time complexity = O(n)
        # space complexity = O(1)
        k %= len(nums)
        nums.reverse()
        for i in range(k//2):
            nums[i], nums[k-1-i] = nums[k-1-i], nums[i]
        for i in range((len(nums) - k)//2):
            nums[k+i], nums[-1-i] = nums[-1-i], nums[k+i]
