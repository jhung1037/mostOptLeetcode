# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time complexity: O(n)
        # space complexity: O(n)
        if not root: return []
        lvl = [root]
        nxt_lvl = []
        res = []
        while lvl:
            res.append([node.val for node in lvl])
            for node in lvl:
                if node.left:
                    nxt_lvl.append(node.left)
                if node.right:
                    nxt_lvl.append(node.right)
            
            lvl = nxt_lvl
            nxt_lvl = []

        res.reverse()
        return res
