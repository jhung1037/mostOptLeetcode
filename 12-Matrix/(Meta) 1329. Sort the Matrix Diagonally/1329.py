class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        row, col = len(mat), len(mat[0])

        sort = collections.defaultdict(list)
        for i in range(row):
            for j in range(col):
                sort[i-j].append(mat[i][j])

        for key, lis in sort.items():
            lis.sort(reverse = True)
            if key <= 0 :
                i, j = 0, -key
            else:
                i, j = key, 0
            while i < row and j < col:
                mat[i][j] = lis.pop()
                i+=1
                j+=1
                
        return mat
