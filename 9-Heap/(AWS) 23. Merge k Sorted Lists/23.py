# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for ll in lists:
            curr = ll
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next
        dummy = ListNode()
        curr = dummy
        while heap:
            curr.next = ListNode(heapq.heappop(heap))
            curr = curr.next
        return dummy.next
