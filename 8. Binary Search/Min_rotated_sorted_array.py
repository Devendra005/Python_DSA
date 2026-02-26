nums = [3,4,5,1,2]
n = len(nums)
low, high = 0, n-1
mini = float("inf")
while low <= high:
    mid = (low + high)//2
    if nums[mid] <= nums[high]:
        mini = min(mini,nums[mid])
        high = mid - 1
    else:
        mini = min(mini,nums[mid])
        low = mid + 1
print(mini)