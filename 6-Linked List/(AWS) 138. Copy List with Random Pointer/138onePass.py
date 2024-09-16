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
            nn = rn = None
            if curr.next:
                if curr.next in ref:
                    nn = ref[curr.next]
                else:
                    nn = Node(curr.next.val)
                ref[curr.next] = nn
            if curr.random:
                if curr.random in ref:
                    rn = ref[curr.random]
                else:
                    rn = Node(curr.random.val)
                ref[curr.random] = rn
            if curr in ref:
                n = ref[curr]
                n.next = nn
                n.random = rn
            else:
                n = Node(curr.val, nn, rn)
            ref[curr] = n
            curr = curr.next
        
        return ref[head]
