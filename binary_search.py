# Intreative soluion 
nums = [-1,0,3,5,9,12]
target = 9

def binarySearch(nums,target):
    n = len(nums)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
print(binarySearch(nums, target))

# Recursive solution 
nums = [-1,0,3,5,9,12]
target = 9

def BS(nums, target, low, high):
    if low > high:
        return -1
    mid = (low + high)//2
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return BS(nums, target, mid + 1, high)
    else:
        return BS(nums, target, low, mid - 1)
print(BS(nums, target, 0, len(nums)-1))