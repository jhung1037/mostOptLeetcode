# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head: return head
        count = 0
        dummy = temp = ListNode(-1,head)
        while temp.next:
            count += 1
            temp = temp.next
        
        k %= count
        if k == 0: return head
        temp.next = dummy.next
        temp = dummy
        for _ in range(count-k):
            temp = temp.next
        
        dummy = temp.next
        temp.next = None

        return dummy