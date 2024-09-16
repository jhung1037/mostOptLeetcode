class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ll = len(nums)
        if ll < 3 : return []

        nums.sort()
        ans = []
        for i, num in enumerate(nums):
            if num > 0: break
            if i > 0 and num == nums[i-1]:
                continue

            l = i + 1
            r = ll - 1
            while l<r:
                tri = num + nums[l] + nums[r]
                if tri > 0:
                    r -= 1
                elif tri < 0:
                    l += 1
                else:
                    ans.append([num, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l<r:
                        l += 1
                    while nums[r] == nums[r+1] and l<r:
                        r -= 1

        return ans
