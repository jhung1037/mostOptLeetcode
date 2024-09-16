class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(31,-1,-1):
            res += (2 ** i) * (n & 1)
            n >>= 1
        return res
