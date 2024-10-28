# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # time complexity = O(n)
    # space complexity = O(logn) ~ O(n)
    def __init__(self):
        self.inorder_max = -math.inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root: return True
        l = self.isValidBST(root.left)

        if not l or self.inorder_max >= root.val:
            return False
        self.inorder_max = root.val
        r = self.isValidBST(root.right)
        return l and r
