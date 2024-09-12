class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = collections.Counter(nums)
        buckets = [[] for i in range(len(nums)+1)]
        for key, value in count.items():
            buckets[value].append(key)

        res = []
        for b in range(len(buckets)-1,0,-1):
            if buckets[b]:
                res.extend(buckets[b])
                if len(res) == k:
                    break
        return res
