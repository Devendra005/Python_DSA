nums = [3,4,4,4,8,9,9,10,12,12,14,15]
target = 11
n = len(nums)
floor = -1
ceil = -1
low = 0
high = n-1
while low <= high:
    mid = (low + high)//2
    if nums[mid] == target:
        floor = nums[mid]
        ceil = nums[mid]
        break
    elif nums[mid] > target:
        ceil = nums[mid]
        high = mid - 1
    else:
        floor = nums[mid]
        low = mid + 1
print([floor,ceil])