# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # time complexity = O(n)
        # space complexity = O(h): O(logn) ~ O(n) -> recursive stack
        res = [root.val]

        def dfs(root):
            if not root: return 0
            left = max(dfs(root.left), 0)
            right = max(dfs(root.right), 0)
            res[0] = max(res[0], root.val + left + right)
            return root.val + max(left, right)
        
        dfs(root)
        return res[0]
