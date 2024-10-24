# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # time complexity = O(nlogk)
        # space complexity = O(1)
        if not lists: return None
        
        def merge2lists(l1, l2):
            dummy = ListNode()
            curr = dummy
            while l1 and l2:
                if l1.val <= l2.val:
                    curr.next = l1
                    l1 = l1.next
                else:
                    curr.next = l2
                    l2 = l2.next
                curr = curr.next
            if not l1:
                curr.next = l2
            else:
                curr.next = l1
            return dummy.next

        while len(lists) > 1:
            res = []
            for i in range(0, len(lists), 2):
                a = lists[i]
                b = lists[i+1] if i+1 < len(lists) else None
                res.append(merge2lists(a, b))
            lists = res
        
        return lists[0]
