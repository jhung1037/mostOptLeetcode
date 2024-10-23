# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # time complexity: O(n)
        # space complexity: O(n)
        curr = head
        count = 0
        stack = []
        while curr:
            count += 1
            stack.append(curr)
            curr = curr.next
        curr = head
        for i in range(count//2):
            tail = stack.pop()
            temp = curr.next
            curr.next = tail
            tail.next = temp
            curr = temp
        curr.next = None
        return head
