class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        index = count = 0
        for i, n in enumerate(nums):
            if n < target: index += 1
            if n == target:
                count += 1

        return [i+index for i in range(count)]
