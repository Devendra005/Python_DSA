nums = [1,1,1,2,3,3,5,6,7,7,7,9,12,12,13]
target = 1
lb = -1
n = len(nums)
low = 0
high = n - 1
while low <= high:
    mid = (low + high)//2
    if nums[mid] >= target:
        lb = mid 
        high = mid - 1
    else:
        low = mid + 1
print(lb)