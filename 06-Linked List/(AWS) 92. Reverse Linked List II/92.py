# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr = head
        par = dummy = ListNode(-1, head)
        left -= 1
        for i in range(left):
            par = curr
            curr = curr.next

        node_before_reverse = par
        first_reverse_node = curr
        reverse_count = right - left
        for i in range(reverse_count):
            temp = curr.next
            curr.next = par
            par = curr
            curr = temp

        node_before_reverse.next = par
        first_reverse_node.next = curr

        return dummy.next
