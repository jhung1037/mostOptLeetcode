class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        while matrix:
            ans += matrix.pop(0)
            rotate = lambda m: list(zip(*m))[::-1]
            matrix = rotate(matrix)
        
        return ans
