class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        cur, cnt, res = 0, 0, [0]*len(boxes)
        for i, c in enumerate(boxes):
            if c == '1':
                cur += i
                cnt -= 1
        for i, c in enumerate(boxes):
            res[i] = cur
            if c == '1':
                cnt += 2
            cur += cnt
        return res