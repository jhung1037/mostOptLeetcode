# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return []

        stack = []
        while True:
            if not root.left and not root.right:
                if stack:
                    root.right = stack.pop()
                    root = root.right
                else: break

            while not root.left and root.right:
                root = root.right
            
            if root.right:
                stack.append(root.right)
            if root.left:
                root.right = root.left
                root.left = None
                root = root.right

        return root
