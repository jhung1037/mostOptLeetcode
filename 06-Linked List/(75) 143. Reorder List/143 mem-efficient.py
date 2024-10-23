# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # time complexity: O(n)
        # space complexity: O(1)
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp

        l, r = head, prev
        while r :
            ltemp = l.next
            rtemp = r.next
            l.next = r
            r.next = ltemp
            l = ltemp
            r = rtemp
        
        # break cycle in odd count
        if l:
            l.next = None

        return head
