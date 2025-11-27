class solution:
    def solve(self, index, total, target, subset, result, nums):
        if total == target:
            result.append(subset.copy())
            return
        if index >= len(nums):
            return
        if total > target:
            return
        Sum = total + nums[index]
        subset.append(nums[index])
        self.solve(index, Sum, target, subset, result, nums)
        Sum = total
        subset.pop()
        self.solve(index + 1, total, target, subset, result, nums)
        
    def combinationSum(self, nums, target):
        result = []
        self.solve(0, 0, target, [], result, nums)
        return result

sol = solution()
nums = [2,3,6,7]    
target = 7
combinations = sol.combinationSum(nums, target)
print("Combinations that sum to", target, "are:", combinations)