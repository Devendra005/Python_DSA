#brute force solution
#time complexity: O(n^3)
arr = [-1,0,1,2,-1,-4]
n = len(arr)
my_set = set()
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if arr[i] + arr[j] + arr[k] == 0:
                temp = [(arr[i], arr[j], arr[k])]
                temp.sort()
                my_set.add(tuple(temp))
print([list(ans) for ans in my_set])

# better solution
# time complexity: O(n^2)
arr = [-1,0,1,2,-1,-4]
n = len(arr)
result = set()
for i in range(n):
    my_set = set()
    for j in range(i+1, n):
        third = -arr[i] - arr[j]
        if third in my_set:
            temp = [arr[i], arr[j], third]
            temp.sort()
            result.add(tuple(temp))
        my_set.add(arr[j])
print([list(ans) for ans in result])

#optimal solution
#time complexity: O(n)
arr = [-1,0,1,2,-1,-4]
ans = []
n = len(arr)
arr.sort()
for i in range(n):
    if i > 0 and arr[i] == arr[i-1]:
        continue
    j = i+1
    k = n-1
    while j < k:
        total_sum = arr[i] + arr[j] + arr[k]
        if total_sum < 0:
            j += 1
        elif total_sum > 0:
            k -= 1
        else:
            temp = [arr[i], arr[j], arr[k]]
            ans.append(temp)
            j += 1
            k -= 1
            while j < k and arr[j] == arr[j - 1]:
                j += 1
            while j < k and arr[j] == arr[k + 1]:
                k -=1
print(ans)

# leetcode - 15
class Solution(object):
    def threeSum(self, nums):
        ans = []
        n = len(nums)
        nums.sort()
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = n-1
            while j < k:
                total_sum = nums[i] + nums[j] + nums[k]
                if total_sum < 0:
                    j += 1
                elif total_sum > 0:
                    k -= 1
                else:
                    temp = [nums[i], nums[j], nums[k]]
                    ans.append(temp)
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[j] == nums[k + 1]:
                        k -=1
        return ans