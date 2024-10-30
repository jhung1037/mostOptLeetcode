# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    # time complexity = O(n)
    # space complexity = O(n)
    def serialize(self, root: TreeNode) -> str:
        
        if not root: return 'N'
        return f"{root.val},{self.serialize(root.left)},{self.serialize(root.right)}"

    def deserialize(self, data: str) -> TreeNode:
        data = data.split(',')
        i = -1
        def dfs():
            nonlocal i
            i += 1
            if data[i] == 'N': return None
            return TreeNode(data[i], dfs(), dfs())
        return dfs()
