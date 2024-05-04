# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val,root)

        def traversal(root, lv, val, depth):

            if lv + 1 == depth:
                root.left = TreeNode(val, root.left, None)
                root.right = TreeNode(val, None, root.right)
                return
            
            if root.left:
                traversal(root.left, lv+1, val, depth)
            if root.right:
                traversal(root.right, lv+1, val, depth)

            return
        traversal(root, 1, val, depth)
        return root
