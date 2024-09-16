class MedianFinder:

    def __init__(self):
        self.maxS = []
        self.minL = []
        self.odd = False

    def addNum(self, num: int) -> None:
        if not self.minL:
            self.minL = [num]
            self.odd = True
            return
        elif not self.maxS:
            if num <= self.minL[0]:
                self.maxS = [-num]
            else:
                self.maxS = [-self.minL[0]]
                self.minL = [num]
            self.odd = False
            return
        
        if self.odd:
            if num <= self.minL[0]:
                heapq.heappush(self.maxS, -num)
            else:
                temp = heapq.heappop(self.minL)
                heapq.heappush(self.maxS, -temp)
                heapq.heappush(self.minL, num)
        else:
            if num >= -self.maxS[0]:
                heapq.heappush(self.minL, num)
            else:
                temp = -heapq.heappop(self.maxS)
                heapq.heappush(self.maxS, -num)
                heapq.heappush(self.minL, temp)
        self.odd ^= 1
        return

    def findMedian(self) -> float:
        if self.odd:
            return float(self.minL[0])
        else:
            return (-self.maxS[0] + self.minL[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()