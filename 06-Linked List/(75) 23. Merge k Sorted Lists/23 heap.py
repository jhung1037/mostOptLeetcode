# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity = O(nlogn)
        # space complexity = O(n)
        heap = []
        index = 0
        for l in lists:
            curr = l
            while curr:
                index += 1
                heapq.heappush(heap, (curr.val, index, curr))
                curr = curr.next
        dummy = curr = ListNode()
        while heap:
            _, _, curr.next = heapq.heappop(heap)
            curr =  curr.next
        return dummy.next
