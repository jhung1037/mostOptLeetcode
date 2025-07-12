# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # time complexity: O(n)
        # space complexity: O(1)
        self.first = self.second = self.prev = None

        def inorder_traversal(root):
            if not root:
                return
            
            inorder_traversal(root.left)

            if self.prev and self.prev.val > root.val:
                if not self.first:
                    self.first = self.prev
                self.second = root
            self.prev = root

            inorder_traversal(root.right)
        
        inorder_traversal(root)
        self.first.val, self.second.val = self.second.val, self.first.val
