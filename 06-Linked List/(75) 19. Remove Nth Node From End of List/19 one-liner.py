class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        return (a:=(b:=(q:=ListNode(0,head))),next(_ for _ in count() if [(b:=b.next) and (n:=n-1)<0 and (a:=a.next)] and not b),setattr(a,'next',a.next.next)) and q.next