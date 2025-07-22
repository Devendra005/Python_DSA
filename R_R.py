#right rotate an array by 1 place
nums = [5,-2,3,9,0,6,10,7]
n = len(nums)
temp = nums[n-1]
for i in range(n-2,-1,-1):
    nums[i+1]=nums [i]
nums[0]=temp
print(temp)



# leetcode 189
class Solution(object):
    def rotate(self, nums, k):
        n = len(nums)
        rotation = k%n
        for _ in range (0,rotations):
            d = nums.pop()
            nums.insert(0,d)
            print(nums)
    print(rotate(0,[1,2,3,4,5,6,7],3))
    