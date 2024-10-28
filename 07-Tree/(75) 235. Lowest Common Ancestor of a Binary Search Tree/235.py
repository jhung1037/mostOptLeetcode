# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # time complexity = O(logn) ~ log(n) = O(h)
        # space complexity = O(logn) ~ log(n) = O(h)
        if p.val > q.val: p, q = q, p

        def dfs(root):
            if p.val <= root.val <= q.val:
                return root
            elif root.val > q.val:
                return dfs(root.left)
            else:
                return dfs(root.right)

        return dfs(root)
