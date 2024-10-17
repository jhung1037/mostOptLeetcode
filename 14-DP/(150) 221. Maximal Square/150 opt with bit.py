class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # time complexity: O(m * n)
        # space complexity: O(len(matrix)) -> create a list of bit represented int
        bits = [int(''.join(row), 2) for row in matrix]
        w = 0
        while bits and any(bits):
            w += 1
            bits = [a & b for a, b in itertools.pairwise(b & (b << 1) for b in bits)]
        return w * w