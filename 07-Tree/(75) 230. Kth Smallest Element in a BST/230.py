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
        self.index = 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root: return None

        l = self.kthSmallest(root.left, k)
        if l is not None: return l

        self.index += 1
        if self.index == k: return root.val

        return self.kthSmallest(root.right, k)
