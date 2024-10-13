class Solution:
    def rob(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(1)
        best = second = 0

        for num in nums:
            new = max(best, second + num)
            second = best
            best = new

        return best
