class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        dic = {}
        maxi = 0
        for num in nums:
            if num in dic:
                continue
            upper = num + 1
            while upper in dic:
                upper = dic[upper][1]
            lower = num - 1
            while lower in dic:
                lower = dic[lower][0]
            dic[num] = [lower, upper]
            maxi = max(upper - lower - 1, maxi)

        return maxi
