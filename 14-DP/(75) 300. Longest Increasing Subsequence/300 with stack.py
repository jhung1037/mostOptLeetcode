class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        stack = []
        for num in nums:
            j = len(stack)-1
            while j >= 0:
                if num > stack[j]:
                    break
                j -= 1
            if j == len(stack)-1:
                stack.append(num)
            else:
                stack[j+1] = num
        return len(stack)
