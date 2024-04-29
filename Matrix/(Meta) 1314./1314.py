class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        row = len(mat)
        col = len(mat[0])
        
        def get_grid(r, c):
            il = r-k if r-k > 0 else 0
            ir = r+k+1 if r+k+1 < row else row
            jl = c-k if c-k > 0 else 0
            jr = c+k+1 if c+k+1 < col else col
            return sum(mat[i][j] for j in range(jl,jr) for i in range(il,ir))

        res = [[0] * col for _ in range(row)]
        for i in range(row):
            for j in range(col):
                res[i][j] = get_grid(i, j)

        return res
