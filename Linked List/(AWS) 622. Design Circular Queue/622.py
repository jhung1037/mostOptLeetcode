class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.front = self.rear  = Node()
        for i in range(1, k):
            n = Node()
            self.rear.next = n
            self.rear = self.rear.next
        self.rear.next = self.front

    def enQueue(self, value: int) -> bool:
        if self.isFull(): return False

        self.rear = self.rear.next
        self.rear.val = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty(): return False

        self.front.val = None
        self.front = self.front.next
        return True

    def Front(self) -> int:
        return -1 if self.front.val is None else self.front.val

    def Rear(self) -> int:
        return -1 if self.rear.val is None else self.rear.val

    def isEmpty(self) -> bool:
        return True if self.front.val is None else False

    def isFull(self) -> bool:
        return True if not self.isEmpty() and self.rear.next == self.front else False


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()