#by k place brute solution 
nums = [3,9,5,6,7,2]
k = 3
n = len(nums)
rotations = k%n
for _ in range (0,rotations):
    d = nums.pop()
    nums.insert(0,d)
    print(nums)
    
    
#better solution 
nums = [1,2,3,4,5,6,7]
k = 3
n = len(nums)
K = k%n
nums [ : ] = nums[n-K: ] + nums[ :n-K]
print(nums)