# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if not n % 2: return []

        dp = {1:[TreeNode()]}

        def dfs(n):
            if n in dp:
                return dp[n]

            poss = []
            for i in range(1, n, 2):
                left = dfs(i)
                right = dfs(n-i-1)
                for l in left:
                    for r in right:
                        root = TreeNode()
                        root.left = l
                        root.right = r
                        poss.append(root)
            dp[n] = poss
            return poss

        return dfs(n)
