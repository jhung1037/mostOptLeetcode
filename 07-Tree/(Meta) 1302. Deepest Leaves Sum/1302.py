# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        d = deque([root])

        while d:
            res = 0
            ll = len(d)
            for i in range(ll):
                root = d.popleft()
                if root.left: d.append(root.left)
                if root.right: d.append(root.right)
                res += root.val
                
        return res