# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # time complexity = O(n)
        # space complexity = O(n) + O(h) = O(n) 
        curr = 0
        ref = {num: i for i, num in enumerate(inorder)}

        def build(l, r):
            if l > r: return None
            nonlocal curr
            root = preorder[curr]
            curr += 1
            return TreeNode(root,
                            build(l, ref[root]-1),
                            build(ref[root]+1, r))

        return build(0, len(preorder)-1)
