num = [1,0,1,1,1]
target = 0
def SearchRotaed(num):
    n = len(num)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if num[mid] == target:
            return True
        if num[mid] <= num[high]:
            if num[mid] <= target <= num[high]:
                low = mid + 1
            else:
                high = mid - 1
        else :
            if num[low] <= target <= num[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return False
print(SearchRotaed(num))


#leetcode -- 81
def search(nums):
    n = len(nums)
    low , high = 0, n-1
    while low <= high:
        mid = (low + high)//2
        if nums[mid] == target:
            return True
        if nums[low] == nums[mid] == nums[high]:
            low += 1
            high -= 1
            continue
        if nums[mid] <= high:
            if nums[mid] <= target <=nums[high]:
                low = mid + 1
            else:
                high = mid - 1
        else:
            if nums[low] <= target <= nums[mid]:
                high = mid -1
            else:
                low = mid + 1
    return False
nums = [1,0,1,1,1]
target = 0
print(search(nums))