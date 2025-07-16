class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # time complexity: O(m * n)
        # space complexity: O(m * n)
        memo = [[-1] * len(matrix[0]) for _ in range(len(matrix))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        def dfs(i, j):
            if memo[i][j] != -1:
                return memo[i][j]
            
            max_len = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                if (0 <= ni < len(matrix) and 0 <= nj < len(matrix[0]) and 
                    matrix[ni][nj] > matrix[i][j]):
                    max_len = max(max_len, 1 + dfs(ni, nj))
            
            memo[i][j] = max_len
            return max_len
        
        return max(dfs(i, j) for i in range(len(matrix)) for j in range(len(matrix[0])))
