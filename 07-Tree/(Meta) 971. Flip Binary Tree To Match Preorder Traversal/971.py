# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:

        q = collections.deque(voyage)
        res = []
        def tra(root):
            if root.val != q.popleft(): return False
            if root.right and root.left and root.right.val == q[0]:
                nonlocal res
                res.append(root.val)
                root.left, root.right = root.right, root.left
            
            if root.left:
                if not tra(root.left): return False
            if root.right:
                if not tra(root.right): return False
            return True
        
        return res if tra(root) else [-1]
