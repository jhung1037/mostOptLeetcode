# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        dummy = ListNode()
        for i in range(len(lists)):
            par = dummy
            a = dummy.next
            b = lists[i]
            while a and b:
                if a.val < b.val:
                    par.next = a
                    a = a.next
                else:
                    par.next = b
                    b = b.next
                par = par.next

            if not a:
                par.next = b
            else:
                par.next = a

        return dummy.next
