class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lst = []
        for num in nums:
            i = bisect_left(lst, num)
            
            if i == len(lst):
                lst.append(num)
            
            else:
                lst[i] = num
        
        return len(lst)
