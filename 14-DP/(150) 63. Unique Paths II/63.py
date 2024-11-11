class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # time complexity = O(m * n)
        # space complexity = O(1)
        if obstacleGrid[0][0]: return 0

        obstacleGrid[0][0] = 1
        for i in range(1, len(obstacleGrid[0])):
            obstacleGrid[0][i] = int(obstacleGrid[0][i-1] == 1 and obstacleGrid[0][i] == 0)
        
        for i in range(1, len(obstacleGrid)):
            obstacleGrid[i][0] = int(obstacleGrid[i-1][0] == 1 and obstacleGrid[i][0] == 0)
        
        for i in range(1, len(obstacleGrid)):
            for j in range(1, len(obstacleGrid[0])):
                if obstacleGrid[i][j]:
                    obstacleGrid[i][j] = 0
                else:
                    obstacleGrid[i][j] = (obstacleGrid[i-1][j] +
                                          obstacleGrid[i][j-1])
        
        return obstacleGrid[-1][-1]
