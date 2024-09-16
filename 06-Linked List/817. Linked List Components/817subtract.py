# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ref = set(nums)
        res = len(ref)
        while head:
            if head.val in ref and head.next and head.next.val in ref:
                res -= 1
            head = head.next
        return res