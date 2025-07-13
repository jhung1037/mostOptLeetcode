# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time complexity: O(n)
        # space complexity: O(n)
        if not root: return []

        lvl_count = 0
        lvl = [root]
        nxt_lvl = []
        res = []
        while lvl:
            res.append([node.val for node in lvl])
            if lvl_count & 1:
                while lvl:
                    node = lvl.pop()
                    if node.left:
                        nxt_lvl.append(node.left)
                    if node.right:
                        nxt_lvl.append(node.right)
            else:
                while lvl:
                    node = lvl.pop()
                    if node.right:
                        nxt_lvl.append(node.right)
                    if node.left:
                        nxt_lvl.append(node.left)
            
            lvl_count += 1
            lvl = nxt_lvl
            nxt_lvl = []
            
        return res
