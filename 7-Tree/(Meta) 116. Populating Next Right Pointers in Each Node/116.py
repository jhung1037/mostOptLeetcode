"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        
        dq = deque([None])
        cur = root

        while cur:
            dq.append(cur.left)
            dq.append(cur.right)

            cur.next = dq.popleft()
            cur = cur.next
            if cur is None:
                dq.append(None)
                cur = dq.popleft()
        
        return root
