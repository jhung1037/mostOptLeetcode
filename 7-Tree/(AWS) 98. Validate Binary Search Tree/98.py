# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        prev = [-math.inf]

        def inorder(node, prev):
            if not node: return True

            if not (inorder(node.left, prev) and prev[0] < node.val):
                return False

            prev[0] = node.val

            return inorder(node.right, prev)

        return inorder(root, prev)
