class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_index = None
        s = 1
        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_index is not None:
                    return [0] * len(nums)
                zero_index = i
            else:
                s *= nums[i]

        if zero_index is not None:
            ans = [s if i == zero_index else 0 for i in range(len(nums))]
        else:
            ans = [int(s / nums[i]) for i in range(len(nums))]

        return ans
