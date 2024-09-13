class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        ans = []
        
        try:
            while True:
                
                p = matrix.pop(0)
                ans += p

                for y in range(len(matrix)):
                    p = matrix[y].pop(-1)
                    ans.append(p)

                p = matrix.pop(-1)
                ans += p[::-1]

                for y in range(len(matrix)-1,-1,-1):
                    p = matrix[y].pop(0)
                    ans.append(p)

        except IndexError:
            return ans
