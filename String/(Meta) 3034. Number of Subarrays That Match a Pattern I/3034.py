class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        comp = [(a<b) - (a>b) for a, b in zip(nums[:-1],nums[1:])]
        l, ll= len(comp), len(pattern)
        return sum(comp[i:i+ll] == pattern for i in range(l-ll+1))