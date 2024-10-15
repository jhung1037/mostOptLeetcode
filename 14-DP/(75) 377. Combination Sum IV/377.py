class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        cache = {}
        nums.sort()

        def dfs(curr):
            if curr < nums[0]:
                cache[curr] = 0
                return cache[curr]
            if curr in cache:
                return cache[curr]
            cache[curr] = 0
            for num in nums:
                if num > curr:
                    break
                elif num == curr:
                    cache[curr] += 1
                    break
                else:
                    cache[curr] += dfs(curr-num)
            return cache[curr]

        return dfs(target)
