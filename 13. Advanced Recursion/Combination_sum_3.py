class solution:
    def solve(self, nums, Sum, index, n, k, result):
        if Sum == n and len(nums) == k:
            result.append(list(nums))
            return
        
        if Sum > n or len(nums) > k:
            return
        
        for i in range(index, 10):
            nums.append(i)
            self.solve(nums, Sum + i, i + 1, n, k, result)
            nums.pop()
        
    def combinationSum3(self, k, n):
        result =[]
        nums = []
        self.solve(nums, 0, 1, n, k, result)
        return result
    
obj = solution()
k = 3
n = 9
print(obj.combinationSum3(k, n))