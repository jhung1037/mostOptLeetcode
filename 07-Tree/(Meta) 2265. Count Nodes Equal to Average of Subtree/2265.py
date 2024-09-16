# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = [0]

        def recur(root):
            if not root: return 0, 0
            
            left_ttl, left_count = recur(root.left)
            right_ttl, right_count = recur(root.right)

            ttl = left_ttl + right_ttl + root.val
            count = left_count + right_count + 1
            if ttl // count == root.val:
                ans[0] += 1

            return ttl, count

        recur(root)
        return ans[0]
