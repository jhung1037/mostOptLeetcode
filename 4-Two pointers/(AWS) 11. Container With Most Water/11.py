class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        width = len(height) - 1
        res = 0
        sh = mh = 0
        for h in height:
            if h > mh:
                sh = mh
                mh = h
            elif h < sh:
                continue
            else:
                sh = h

        while l < r:
            if height[l] < height[r]:
                res = max(res, width * height[l])
                l += 1
            else:
                res = max(res, width * height[r])
                r -= 1
            if sh * width <= res:
                break
            width -= 1

        return res
