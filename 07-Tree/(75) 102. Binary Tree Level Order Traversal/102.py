# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time complexity = O(n)
        # space complexity = O(w): O(1) ~ O(n/2) -> O(n)
        if not root: return []
        queue = [root]
        res = []
        while queue:
            new_q = []
            lv = []
            for node in queue:
                lv.append(node.val)
                if node.left:
                    new_q.append(node.left)
                if node.right:
                    new_q.append(node.right)
            res.append(lv)
            queue = new_q

        return res
