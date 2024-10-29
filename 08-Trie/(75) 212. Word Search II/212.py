class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # time complexity = O(m * n * 4^Length) + O(Words * Length) = O(M * N * 4^L + W * L)
        # space complexity = O(Length: recursive depth) + O(Words * Length) = O(W * L)
        '''
        Remove impossible or visited node to reduce duplicate search.
        Temporarily mark the board with '*' to save the space for visited set().
        '''
        ROWS, COLS = len(board), len(board[0])
        trie = {}
        for i, word in enumerate(words):
            curr = trie
            for c in word:
                if c not in curr:
                    curr[c] = {}
                curr = curr[c]
            curr['#'] = i

        res = []
        def dfs(r, c, curr):
            if (not (0 <= r < ROWS) or
                not (0 <= c < COLS) or
                board[r][c] not in curr):
                return
            char = board[r][c]
            if '#' in curr[char]:
                res.append(words[curr[char]['#']])
                del curr[char]['#']

            board[r][c] = '*'
            dfs(r-1, c, curr[char])
            dfs(r, c-1, curr[char])
            dfs(r, c+1, curr[char])
            dfs(r+1, c, curr[char])
            board[r][c] = char

            if not curr[char]:
                del curr[char]

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie)
        
        return res
