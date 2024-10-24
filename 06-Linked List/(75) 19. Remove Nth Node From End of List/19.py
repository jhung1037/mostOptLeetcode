# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # time complexity = O(n)
        # space complexity = O(1)
        slow = fast = dummy = ListNode(-1, head)

        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next if slow.next is not None else None

        return dummy.next
