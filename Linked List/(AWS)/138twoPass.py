"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        curr = head
        ref = {None: None}
        while curr:
            n = Node(curr.val)
            ref[curr] = n
            curr = curr.next
        curr = head
        while curr:
            ref[curr].next = ref[curr.next]
            ref[curr].random = ref[curr.random]
            curr = curr.next
        
        return ref[head]
