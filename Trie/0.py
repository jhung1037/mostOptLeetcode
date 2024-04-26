


def ans(nums):
    if len(nums) == 1:
        return 0
    if nums[0] > nums[1]:
        return 0
    if nums[-1] > nums[-2]:
        return len(nums)-1

    for i in range(1, len(nums)-1):
        if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
            return i
        
print(ans([1,2,3,1]))