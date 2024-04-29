class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        row = len(land)
        col = len(land[0])
        
        res = []
        i = 0
        while i < row:
            j = 0
            while j < col:
                if land[i][j]:
                    ni = i
                    while ni < row and land[ni][j]:
                        nj = j
                        while nj < col and land[ni][nj]:
                            land[ni][nj] = 0
                            nj+=1
                        ni+=1
                    res.append([i,j,ni-1,nj-1])
                j+=1
            i+=1

        return res
