# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left: return root
        def dfs(left,right, odd):
            if odd:
                left.val, right.val = right.val, left.val
            if left.left:
                dfs(left.left, right.right, odd ^ 1)
                dfs(left.right, right.left, odd ^ 1)

        dfs(root.left, root.right, 1)
        return root