class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # time complexity: O(n)
        # space complexity: O(n)
        dic = {}
        maxi = 0
        for num in nums:
            if num in dic: continue
            upper = dic[num + 1][1] if num + 1 in dic else num
            lower = dic[num - 1][0] if num - 1 in dic else num
            dic[num] = [lower, upper]
            dic[upper][0] = lower
            dic[lower][1] = upper
            maxi = max(upper - lower + 1, maxi)

        return maxi
