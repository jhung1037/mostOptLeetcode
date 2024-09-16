class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = -math.inf
        curr_max, curr_min = 1, 1

        for n in nums:
            temp = curr_max
            curr_max = max(curr_max*n, curr_min*n, n)
            curr_min = min(temp*n, curr_min*n, n)
            res = max(res, curr_max)
        
        return res
