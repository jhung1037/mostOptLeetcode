class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)

        heap = []
        for key, value in dic.items():
            heapq.heappush(heap,[-value, key])
        
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])

        return res
