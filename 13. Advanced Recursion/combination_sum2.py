class solution:
    def solve(self, subset, index, target, result, nums):
        if target == 0:
            result.append(subset.copy())
            return
        
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            
            if nums[i] > target:
                break
            
            subset.append(nums[i])
            self.solve(subset, i + 1, target - nums[i], result, nums)
            subset.pop()
    
    def combinationSum2(self, nums, target):
        nums.sort()
        result = []
        self.solve([], 0, target, result, nums)
        return result
    
sol = solution()
nums = [1,1,2,1,2]
target = 4
combinations = sol.combinationSum2(nums, target)
print("Unique combinations that sum to", target, "are:", combinations)
