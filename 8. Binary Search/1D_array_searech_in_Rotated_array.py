#brute solution 
nums = [1,4,5,6,8,9,10,11,15,20]
target = 6
n = len(nums)
def SearchRotatedArray(nums):
    for i in range(0,n):
        if nums[i] == target:
            return i
    return -1
print(SearchRotatedArray(nums))

#optimnal solution 
num = [17,18,20,1,3,4,5,7,8,10,11,13,14,16]
target = 4
def SearchRotaed(num):
    n = len(num)
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high)//2
        if num[mid] == target:
            return mid
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
    return -1
print(SearchRotaed(num))