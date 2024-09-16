# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = sdummy = ListNode()
        dummy2 = ldummy = ListNode()
        while head:
            if head.val < x:
                sdummy.next = head
                sdummy = sdummy.next
            else:
                ldummy.next = head
                ldummy = ldummy.next
            head = head.next

        ldummy.next = None
        sdummy.next = dummy2.next
        return dummy.next
