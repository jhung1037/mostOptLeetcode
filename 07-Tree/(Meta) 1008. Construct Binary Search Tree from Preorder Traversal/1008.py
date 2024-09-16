# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        if N == 0: return None
        if N == 1: return TreeNode(preorder[0])
        
        l = 1
        h = N - 1
        while l <= h :
            m = (l+h) // 2
            if preorder[m] > preorder[0] and preorder[m-1] <= preorder[0]:
                break
            if preorder[m] > preorder[0]:
                h = m - 1
            else:
                l = m + 1

        if l > h: m += 1

        return TreeNode(
            preorder[0],
            self.bstFromPreorder(preorder[1:m]),
            self.bstFromPreorder(preorder[m:]),
        )
