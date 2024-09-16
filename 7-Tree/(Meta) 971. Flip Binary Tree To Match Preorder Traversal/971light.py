# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        self.res = []
        self.index = 0
        def valid(root):
            if not root: return True
            if root.val != voyage[self.index]: return False
            self.index += 1
            if root.left and root.right and root.right.val == voyage[self.index]:
                self.res.append(root.val)
                return valid(root.right) and valid(root.left)
            return valid(root.left) and valid(root.right)

        return self.res if valid(root) else [-1]
