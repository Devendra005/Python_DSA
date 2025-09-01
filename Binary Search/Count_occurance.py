nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
target = 3
n = len(nums)
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
print(last-first+1)

#optimal Solution 
class Solution(object):
    def lowerBound(self, nums, target):
        n = len(nums)
        low = 0 
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def upperBound(self, nums, target):
        n = len(nums)
        low = 0
        high = n - 1
        ans = n
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans

    def searchRange(self, nums, target):
        lb = self.lowerBound(nums, target)
        if lb == len(nums) or nums[lb] != target:
            return [-1, -1]
        ub = self.upperBound(nums, target)
        return ub - lb

if __name__ == "__main__":
    nums = [1,2,3,3,3,3,3,5,6,8,9,9,10]
    target = 3
    sol = Solution()
    print(sol.searchRange(nums, target))
    