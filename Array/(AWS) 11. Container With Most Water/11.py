class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        width = len(height) - 1
        res = 0
        mh = max(height)
        while l < r:
            if height[l] < height[r]:
                res = max(res, width * height[l])
                l += 1
            else:
                res = max(res, width * height[r])
                r -= 1
            if mh * width <= res:
                break
            width -= 1

        return res
