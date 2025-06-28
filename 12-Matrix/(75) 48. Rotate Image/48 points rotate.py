class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # time complexity = O(n^2)
        # space complexity = O(1)
        for i in range(len(matrix)//2):
            t, l, b, r = i, i, len(matrix)-1-i, len(matrix[0])-1-i
            offset = 0
            while l + offset < r:
                temp = matrix[t][l+offset]
                matrix[t][l+offset] = matrix[b-offset][l]
                matrix[b-offset][l] = matrix[b][r-offset]
                matrix[b][r-offset] = matrix[t+offset][r]
                matrix[t+offset][r] = temp
                offset += 1
