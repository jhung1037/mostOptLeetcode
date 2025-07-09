class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # time complexity: O(L1 + L2)
        # space complexity: O(L1) => worst case: O(L1 + L2)
        if len(nums2) == 1: return [-1]

        ref = {num: i for i, num in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = [nums2[0]]
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                num = stack.pop()
                if num in ref:
                    res[ref[num]] = nums2[i]
            stack.append(nums2[i])
        
        return res
