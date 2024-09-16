class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n
        right_ball = 0
        right_moves = 0
        left_ball = 0
        left_moves = 0

        for i in range(n):
            if boxes[i] == '1':
                right_moves += i + 1
                right_ball += 1


        for i in range(n):
            right_moves -= right_ball
            res[i] = right_moves + left_moves
            
            if boxes[i] == '1':
                right_ball -= 1
                left_ball += 1
            
            left_moves += left_ball

        return res
