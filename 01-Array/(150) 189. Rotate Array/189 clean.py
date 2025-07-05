class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        # time complexity = O(n)
        # space complexity = O(1)
        def _reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        k %= len(nums)
        _reverse(0, len(nums)-1)
        _reverse(0, k-1)
        _reverse(k, len(nums)-1)
