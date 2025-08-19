#brute solution 
nums = [1,0,2,4,3,0,0,3,5,1]

n=len(nums)
temp =[]
for i in range(0,n):
    if nums[i]!=0:
        temp.append(nums[i])
nz = len(temp)
for i in range(0,nz):
    nums[i]=temp[i]
for i in range(nz,n):
    nums[i] = 0
print(nums)

#optimal solution 
def move_zeros_end(nums):
    if len(nums) == 1:
        return
    i = 0
    while i < len(nums):
        if nums[i] == 0:
            break
        i+=1
    if i == len(nums):
        return
    j = i+1
    while j < len(nums):
        if nums[j]!=0:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1    
        j+=1
move_zeros_end(nums)
print(nums)


#leetCode 283
def moveZeroes(self, nums):
    n = len(nums)
    last_non_zero = 0
        
# Move all non-zero elements to the front
    for i in range(n):
        if nums[i] != 0:
            nums[last_non_zero], nums[i] = nums[i], nums[last_non_zero]
            last_non_zero += 1
moveZeroes(0,nums)
print(nums)