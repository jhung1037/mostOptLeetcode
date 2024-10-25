# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # time complexity = O(n)
        # space complexity = ∑O(w) + O(h) = O(n) + O(h) = O(n)
        if not preorder: return None
        i = inorder.index(preorder[0])
        return TreeNode(preorder[0],
                        self.buildTree(preorder[1:i+1], inorder[:i]),
                        self.buildTree(preorder[i+1:], inorder[i+1:]))
