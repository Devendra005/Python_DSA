# brute solution O(n^4)
nums = [1,0,-1,0,-2,2,5,9]
n = len(nums)
target = 0
def fourSum(target):
    if n < 4 :
        return []
    my_set = set()
    for i in range(0,n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                for l in range(k+1,n):
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target:
                        temp = [nums[i],nums[j],nums[k],nums[l]]
                        temp.sort()
                        my_set.add(tuple(temp))
    result = []
    for ans in my_set:
        result.append(list(ans))
    return result
print(fourSum(0))

# Better solution O(N^3)
def fourSumBetter(target):
    my_set = set()
    for i in range(0,n):
        for j in range (i+1,n):
            has_set = set()
            for k in range(j+1,n):
                fourth = target - (nums[i]+nums[j]+nums[k])
                if fourth in has_set:
                    temp = [nums[i],nums[j],nums[k],fourth]
                    temp.sort()
                    my_set.add(tuple(temp))
                has_set.add(nums[k])
    result = []
    for ans in my_set:
        result.append(list(ans))
    return result
print(fourSumBetter(0))

# Optimal Solution
def fourSumOptimal(target):
    nums = [1,0,-1,0,-2,2]
    ans = []
    nums.sort()
    n = len(nums)
    for i in range(0,n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1,n):
            if j > i+1 and nums[j] == nums[j-1]:
                continue 
            k = j+1
            l = n-1
            while k < l:
                total = nums[i]+nums[j]+nums[k]+nums[l]
                if total == target:
                    ans.append([nums[i],nums[j],nums[k],nums[l]])
                    k += 1
                    l -= 1
                    while k > l and nums[k] == nums[k-1]:
                        k += 1
                    while l > k and nums[l] == nums[l+1]:
                        l -= 1
                elif total < target:
                    k += 1
                else:
                    l -= 1
    return ans

print(fourSumOptimal(0))