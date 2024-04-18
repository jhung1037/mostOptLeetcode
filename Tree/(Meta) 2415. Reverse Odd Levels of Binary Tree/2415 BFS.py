# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        odd = 0

        dq = deque([root])
        stack = []

        while dq:
            dl = len(dq)
            stack = []
            for i in range(dl):
                node = dq.popleft()
                if odd:
                    stack.append(node)
                if node.left: dq.append(node.left)
                if node.right: dq.append(node.right)

            if odd:
                ll = len(stack)
                for i in range(ll//2):
                    stack[i].val, stack[ll-i-1].val = stack[ll-i-1].val, stack[i].val
            
            odd ^= 1

        return root
