class solution:
    def solve(self, index, total, result, nums):
        if index >= len(nums):
            result.append(total)
            return
        Sum = total + nums[index]
        self.solve(index + 1, Sum, result, nums)
        Sum = total
        self.solve(index + 1, Sum, result, nums)
        
    def subsetSum(self, nums):
        result = []
        self.solve(0, 0, result, nums)
        result.sort()
        return result
    
obj = solution()
nums = [5, 9, 3]
print(obj.subsetSum(nums))