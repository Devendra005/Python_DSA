nums = [5,10,-3,-1,-10,6]
def rearrangeArray(nums):
    n = len(nums)
    result = [0]*n
    posIdx ,negIdx = 0,1
    for i in range(0,n):
        if nums[i] >= 0:
            result[posIdx] = nums[i]
            posIdx += 2
        else :
            result[negIdx] = nums[i]
            negIdx += 2
    return result
print(rearrangeArray(nums))