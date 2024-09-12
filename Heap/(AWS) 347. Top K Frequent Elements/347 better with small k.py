class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = collections.Counter(nums)

        heap = []
        for key, value in dic.items():
            heapq.heappush(heap,[value, key])
            if len(heap) > k:
                heapq.heappop(heap)

        return [i[1] for i in heap]
