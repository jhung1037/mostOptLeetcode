# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        self.index = 0
        self.N  = len(preorder)

        def helper(lower, upper):
            if self.index >= self.N:
                return None
            
            val = preorder[self.index]
            if lower > val or val > upper:
                return None

            root = TreeNode(val)
            self.index += 1
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        
        return helper(-math.inf, math.inf)