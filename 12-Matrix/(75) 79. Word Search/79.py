class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # time complexity = O(n^2 * 3^L)
        # space complexity = O(L)
        if len(word) > len(board) * len(board[0]):
            return False

        count = Counter(sum(board, []))

        for char, num in Counter(word).items():
            if char not in count or count[char] < num:
                return False
            
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        direct = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        visited = set()
        
        def dfs(index, i, j):
            if ((i, j) in visited
                or not 0 <= i < len(board)
                or not 0 <= j < len(board[0])):
                return False
            if word[index] == board[i][j]:
                if index == len(word) - 1:
                    return True
                visited.add((i, j))
                for r, c in direct:
                    if dfs(index+1, i+r, j+c):
                        return True
                visited.discard((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(0, i, j):
                    return True
        return False
