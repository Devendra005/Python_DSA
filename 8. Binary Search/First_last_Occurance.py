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
        return [lb, ub - 1]

if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 8, 10]
    target = 8
    sol = Solution()
    print(sol.searchRange(nums, target))
    

# Brute solution 
n = len(nums)
first = -1
last = -1
for i in range(0,n):
    if nums[i] == target:
        if first == -1:
            first = i
        last = i
print([first,last])