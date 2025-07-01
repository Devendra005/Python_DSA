nums = [5,7,3,2,6,1,5,9]

def func(nums,left,right):
    if left >= right:
        return
    nums[left],nums[right] = nums[right],nums[left]
    func(nums,left+1,right-1)
def reverseArray(nums,l,r):
    func(nums,l,r)
    return nums
print(reverseArray(nums,0,len(nums)-1))

# Using while loop
def fun(nums,l,r):
    while l < r:
        nums[l],nums[r] = nums[r],nums[l]
        l +=1
        r -=1
    return nums
print(fun(nums,0,len(nums)-1))