# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        ref = set(nums)
        res = 0
        connected = False
        while head:
            if head.val in ref:
                if not connected:
                    res += 1
                head = head.next
                connected = True
            else:
                head = head.next
                connected = False
        return res