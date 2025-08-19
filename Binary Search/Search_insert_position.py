nums = [1,3,4,5,8,9,14,15,19,20,21]
target = 5
n = len(nums)
low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] < target:
        low = mid + 1
    else:
        high = mid - 1
print(low)